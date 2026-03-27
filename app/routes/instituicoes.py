from flask import Blueprint, request, jsonify
from app.services.instituicao_service import *
from app.services.supabase_service import get_supabase

instituicoes_bp = Blueprint("instituicoes", __name__)

# 🔥 LISTAR
@instituicoes_bp.route("/instituicoes", methods=["GET"])
def listar():
    estado = request.args.get("estado")

    if estado:
        data = buscar_por_estado(estado)
    else:
        data = listar_instituicoes()

    return jsonify(data)


# 🔥 BUSCAR POR ID (FALTAVA)
@instituicoes_bp.route("/instituicoes/<id>", methods=["GET"])
def buscar(id):
    supabase = get_supabase()

    data = supabase.table("instituicoes") \
        .select("*") \
        .eq("id", id) \
        .single() \
        .execute().data

    return jsonify(data)


# 🔥 CRIAR
@instituicoes_bp.route("/instituicoes", methods=["POST"])
def criar():
    body = request.json
    data = criar_instituicao(body)
    return jsonify(data)


# 🔥 ATUALIZAR (ADMIN - APROVAR/REJEITAR)
@instituicoes_bp.route("/instituicoes/<id>", methods=["PUT"])
def atualizar(id):
    body = request.json
    supabase = get_supabase()

    data = supabase.table("instituicoes") \
        .update(body) \
        .eq("id", id) \
        .execute().data

    return jsonify(data)


# 🔥 DELETAR
@instituicoes_bp.route("/instituicoes/<id>", methods=["DELETE"])
def deletar(id):
    data = deletar_instituicao(id)
    return jsonify(data)