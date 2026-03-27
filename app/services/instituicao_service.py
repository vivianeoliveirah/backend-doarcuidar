from app.services.supabase_service import get_supabase


def listar_instituicoes():
    supabase = get_supabase()
    return supabase.table("instituicoes").select("*").execute().data


def buscar_por_estado(estado):
    supabase = get_supabase()
    return supabase.table("instituicoes").select("*").eq("estado", estado).execute().data


def criar_instituicao(data):
    supabase = get_supabase()
    return supabase.table("instituicoes").insert(data).execute().data


def deletar_instituicao(id):
    supabase = get_supabase()
    return supabase.table("instituicoes").delete().eq("id", id).execute().data