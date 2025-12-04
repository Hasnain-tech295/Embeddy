# Embeddy
Embedding playground for everything 🤗

Minimal starter for a small embeddings + vector-store playground:
FastAPI backend, Supabase (pgvector) integration, local embedding model (sentence-transformers),
and a tiny static frontend.

Run locally:
1. Copy `.env.example` to `.env` and fill values.
2. `pip install -r requirements.txt`
3. `uvicorn src.app.main:app --reload --port 8000`
4. Open `frontend/static/index.html`.

This repo contains minimal starter implementations — intended for learning and extension.
