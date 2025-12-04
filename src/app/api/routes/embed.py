# / embed endpoints
from fastapi import APIRouter
from pydantic import BaseModel
from src.services.embeddings import get_embeddings

router = APIRouter()

class EmbeddinRequest(BaseModel):
    texts: list[str]
    model: str
    

class EmbeddinResponse(BaseModel):
    embeddings: list[list[float]]
    model: str
    usage: dict[str, int]

@router.post("/", response_model=EmbeddinResponse)
async def embed_text(req: EmbeddinRequest):
    embeddings = []
    for t in req.texts:
        emb = await get_embeddings(t)
        embeddings.append(emb)
    
    return {"embeddings": embeddings}