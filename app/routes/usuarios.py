from flask import Blueprint, request, jsonify
from app.services.usuario_service import *

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios", methods=["GET"])
def listar():
    return jsonify(listar_usuarios())


@usuarios_bp.route("/usuarios", methods=["POST"])
def criar():
    data = criar_usuario(request.json)
    return jsonify(data)