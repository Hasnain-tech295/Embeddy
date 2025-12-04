# text chunking and overlap helper
from typing import List

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """
    Basic greedy chunker that splits on whitespace. Not smart about sentences - simple starter
    """
    words = text.split()
    chunks = []
    i = 0
    n = len(words)
    while i < n:
        chunk = words[i: i+chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap
    
    return chunks