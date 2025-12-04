# low level db client integraton
from supabase import create_client
from src.core.config import get_settings

_settings = get_settings()
_client = None

def get_supabase_client():
    global _client
    if _client is None:
        if not _settings.SUPABASE_URL or not _settings.SUPABASE_KEY:
            raise RuntimeError("Supabase config not found in environment.")
        _client = create_client(_settings.SUPABASE_URL, _settings.SUPABASE_KEY)
    return _client