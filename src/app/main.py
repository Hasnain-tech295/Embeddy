# FastAPI app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import logging

# Importing route modules
from src.app.api.routes.embed import router as embed_router
from src.app.api.routes.insert import router as insert_router
from src.app.api.routes.query import router as query_router
from src.core.config import get_settings

logger = logging.getLogger("uvicorn.error")
settings = get_settings()

def create_app() -> FastAPI:
    app = FastAPI(
        title="Embeddings Playground",
        description="Minimal RAG + Embeddings backend",
        version="0.1.0"
    )
    
    # ------------CORS (all all for dev; lock down in production)-----------
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],   # In production, restricted to fronend domain
        allow_credentials = True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # ------------Mount Static frontend -----------
    try:
        app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
    except Exception as e:
        logger.debug("Could not mount static files: %s", e)
    
    # -----------ROUTES------------
    app.include_router(embed_router, prefix="/api/embed", tags=["embed"])
    app.include_router(insert_router, prefix="/api/insert", tags=["insert"])
    app.include_router(query_router, prefix="/api/query", tags=["query"])
    
    @app.get("/")
    async def root():
        return {
            "status": "running",
            "project": "Embeddings Playground",
            "environment": getattr(settings, "EMBEDDING_MODEL", None),
        }
        
    return app

# Uvicorn entry point
app = create_app()