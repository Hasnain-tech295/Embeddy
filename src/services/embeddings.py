# wrapper for embedding model, API
import asyncio
from sentence_transformers import SentenceTransformer
from src.core.config import get_settings

_settings = get_settings()
_model = None
def _load_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(_settings.EMBEDDING_MODEL)
        
    return _model

async def get_embeddings(text: str) -> list[float]:
    """
    Returns a dense vector for`text`.
    This wrapper is async-friendly by running the CPI-bound call in a thread pool.
    """
    loop = asyncio.get_running_loop()
    model = await loop.run_in_executor(None, _load_model)
    emb = await loop.run_in_executor(None, model.encode, text, True)
    #model.encode returns numpy array - convert to list
    return emb.tolist()