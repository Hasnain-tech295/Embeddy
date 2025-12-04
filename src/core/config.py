# central config loader (env)

from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL: str | None = None
    SUPABASE_KEY: str | None = None
    DATABASE_URL: str | None = None
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    LOCAL_EMBEDDING: bool = True
    
    class config:
        env_file = ".env"
    
@lru_cache()
def get_settings():
    return Settings()