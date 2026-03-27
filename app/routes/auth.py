from flask import Blueprint, request, jsonify
from app.services.supabase_service import get_supabase

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/auth/login", methods=["POST"])
def login():
    supabase = get_supabase()
    body = request.json

    response = supabase.auth.sign_in_with_password({
        "email": body["email"],
        "password": body["password"]
    })

    return jsonify(response.user)


@auth_bp.route("/auth/register", methods=["POST"])
def register():
    supabase = get_supabase()
    body = request.json

    response = supabase.auth.sign_up({
        "email": body["email"],
        "password": body["password"]
    })

    return jsonify(response.user)