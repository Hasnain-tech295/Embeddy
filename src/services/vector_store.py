# # pg vecor, supabase access helper

from typing import List, Dict, Any
from src.core.config import get_settings
from src.db.supabase_client import get_supabase_client

settings = get_settings()

async def upsert_vectors(items: List[Dict[str, Any]]) -> bool:
    """
    items: [{"id": str, "embedding": [...], "metadata": {...}}, ...]
    Minimal async wrapper for Supabase insertion/upsertion
    """
    sb = get_supabase_client()
    ## supabase-py is sync-ish; this is a simplified wrapper (callers can run in thread pool if needed)
    try:
        # Table name embeddings
        data = [{"id": it[id], "embedding": it["embedding"], "metadata": it["metadata"]} for it in items]
        resp = sb.table("embeddings").upsert(data).execute()
        return resp.status_code in (200, 201)
    
    except Exception as e:
        print(f"Error upserting vectors: {e}")
        return False

async def query_vectors(query_embedding: List[float], top_k: int = 5):
    """
    Minimal query via Supabase SQL / RPC or vector extention
    For starter: calls a simple RPC or uses 'match' if configured.
    Returns list of dicts: {"id", "score", "metadata"} 

    """
    sb = get_supabase_client()
    try:
        # This demonstrates the idea — many Supabase setups will use raw SQL with pgvector <-> '<->' operator.
        # For a starter, we call a simple RPC named 'match_embeddings' (you can create it in infra scripts).
        payload = {"Query_embedding": query_embedding, "match_count": top_k}
        resp = sb.rpc("match_embeddings", payload).execute()
        return resp.data
    except Exception as e:
        print(f"Error querying vectors: {e}")
        return []