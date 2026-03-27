from app.services.supabase_service import get_supabase

def listar_usuarios():
    supabase = get_supabase()
    return supabase.table("usuarios").select("*").execute().data


def criar_usuario(data):
    supabase = get_supabase()
    return supabase.table("usuarios").insert(data).execute().data