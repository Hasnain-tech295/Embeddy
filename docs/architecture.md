# Architecture (minimal)

- FastAPI serves three main routes: /embed, /insert, /query
- Embedding service uses sentence-transformers locally (or remote API)
- Vector store: Supabase Postgres + pgvector
- Frontend: static HTML + small JS calls to /query
- Background jobs: simple async tasks (later: Celery / RQ)
