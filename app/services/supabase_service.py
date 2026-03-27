from supabase import create_client
from app.config import Config

def get_supabase():
    if not Config.SUPABASE_URL:
        raise Exception("SUPABASE_URL não carregada")

    return create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)