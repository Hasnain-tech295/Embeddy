import pytest
from src.services.embeddings import get_embedding

@pytest.mark.asyncio
async def test_embedding_length():
    emb = await get_embedding("hello world")
    assert isinstance(emb, list)
    assert len(emb) > 0