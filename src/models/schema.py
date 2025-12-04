# pydantic request/response model
from pydantic import BaseModel
from typing import Any, Dict, List

class UpsertItem(BaseModel):
    id: str
    embedding: List[float]
    metadata: Dict[str, Any]