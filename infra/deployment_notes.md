# Deployment notes (Railway + Vercel)

## Backend (FastAPI) -> Railway
1. Create a Railway project and link your GitHub repo or push the code.
2. Add environment variables:
   - SUPABASE_URL, SUPABASE_KEY, DATABASE_URL, EMBEDDING_MODEL, LOCAL_EMBEDDING=false (if using remote embeddings).
3. Railway will detect Python and run `uvicorn src.app.main:app --host 0.0.0.0 --port $PORT`.
4. Set up persistent files or use managed Supabase for vectors (recommended).
5. Use service_role key stored in Railway secrets for upsert operations.

## Frontend (static) -> Vercel
1. Deploy `frontend/static` as a Vercel project (connect GitHub and point to that folder).
2. If your backend is hosted at `https://my-backend.railway.app`, configure it in the front-end JS or set up a proxy.
3. If cross-origin issues occur, add CORS in FastAPI:
   ```py
   from fastapi.middleware.cors import CORSMiddleware
   app.add_middleware(CORSMiddleware, allow_origins=["*"])
