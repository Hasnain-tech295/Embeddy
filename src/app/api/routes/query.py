# /query endpoint
from fastapi import APIRouter
from pydantic import BaseModel
from src.services.embeddings import get_embeddings
from src.services.vector_store import query_vectors

router = APIRouter()

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5
    
@router.post("/")
async def query(req: QueryRequest):
    q_emb = await get_embeddings(req.query)
    results = await query_vectors(q_emb, top_k=req.top_k)
    return {"results": results}
