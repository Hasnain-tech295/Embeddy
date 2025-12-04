# /insert endpoint
from fastapi import APIRouter, HTTPException, UploadFile, File, Form, BackgroundTasks
from pydantic import BaseModel
from typing import List
import io
import pdfplumber

from src.utils.chunking import chunk_text
from src.services.embeddings import get_embeddings
from src.services.vector_store import upsert_vectors

router = APIRouter()

# Keep a simple JSON endpoint for programmatic clients if needed
class InsertRequest(BaseModel):
    doc_id: str
    text: str

@router.post("/", summary="Upload a file or text for insertion")
async def insert_document_file(
    background_tasks: BackgroundTasks,
    doc_id: str = Form(...),
    file: UploadFile = File(...),
):
    """
    Accepts a file (PDF or TXT). Extracts text and schedules background indexing.
    Returns quickly with accepted status.
    """
    # Read file bytes
    try:
        contents = await file.read()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to read file: {e}")

    # Extract text depending on mime / extension
    text = ""
    content_type = (file.content_type or "").lower()
    filename = (file.filename or "").lower()
    try:
        if "pdf" in content_type or filename.endswith(".pdf"):
            # Use pdfplumber on in-memory bytes
            with io.BytesIO(contents) as bio:
                with pdfplumber.open(bio) as pdf:
                    pages = [p.extract_text() or "" for p in pdf.pages]
                    text = "\n".join(pages)
        else:
            # treat as plain text
            text = contents.decode("utf-8", errors="ignore")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to extract text: {e}")

    if not text.strip():
        raise HTTPException(status_code=400, detail="No text extracted from file")

    # Chunk the text
    chunks = chunk_text(text, chunk_size=500, overlap=50)

    # Schedule background task for embedding/upsert to avoid blocking upload
    background_tasks.add_task(_background_embed_and_upsert, doc_id, chunks)
    # fast response
    return {"status": "accepted", "inserted_chunks": len(chunks)}

# keep original JSON insertion route for completeness
@router.post("/text", summary="Insert raw text (JSON)")
async def insert_document_text(req: InsertRequest):
    chunks = chunk_text(req.text, chunk_size=500, overlap=50)
    await _background_embed_and_upsert(req.doc_id, chunks)
    return {"inserted_chunks": len(chunks)}

# Background worker function
async def _background_embed_and_upsert(doc_id: str, texts: List[str]):
    """
    Compute embeddings (concurrently) and upsert into vector store.
    Runs in event loop; keep it simple for Phase 0. For heavy loads use Celery/RQ.
    """
    # compute embeddings concurrently
    embeddings = await _batch_get_embeddings(texts)
    items = []
    for i, emb in enumerate(embeddings):
        items.append({"id": f"{doc_id}-{i}", "embedding": emb, "metadata": {"doc_id": doc_id, "index": i, "text": texts[i]}})
    # upsert into vector store
    ok = await upsert_vectors(items)
    return ok

async def _batch_get_embeddings(texts: List[str]):
    # simple concurrency: kick off tasks and await them
    tasks = [get_embeddings(t) for t in texts]
    results = await __gather_tasks_safely(tasks)
    return results

async def __gather_tasks_safely(tasks):
    # gather but continue on individual failures (return empty vector if failed)
    import asyncio
    gathered = await asyncio.gather(*tasks, return_exceptions=True)
    out = []
    for r in gathered:
        if isinstance(r, Exception):
            # fallback to small empty vector — better to log in production
            out.append([0.0])  
        else:
            out.append(r)
    return out
