# background task
import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import List
from src.services.embeddings import get_embedding
from src.services.vector_store import upsert_vectors

_executor = ThreadPoolExecutor(max_workers=4)

async def batch_upsert_texts(doc_id: str, texts: List[str]):
    """
    Example background task: compute embeddings for texts and upsert them.
    For real usage, vall this via FastAPI's background tasks or Celery.
    """
    
    tasks = []
    for i, t in enumerate(texts):
        tasks.append(get_embedding(t))
        
    embeddings = await asyncio.gather(*tasks)
    
    items = []
    for i, emb in enumerate(embeddings):
        items.append({"id": f"{doc_id}-{i}", "embedding": emb, "metadata": {"doc_id": doc_id, "index": i}})
        
    ok = await upsert_vectors(items)
    return ok