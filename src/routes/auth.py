from flask import Blueprint, request, jsonify
from src.models.usuario import Usuario
from werkzeug.security import check_password_hash
import jwt
import datetime
import os

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    senha = data.get("senha")

    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario or not check_password_hash(usuario.senha, senha):
        return jsonify({"error": "Credenciais inválidas"}), 401

    token = jwt.encode(
        {
            "id": usuario.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        os.getenv("SECRET_KEY", "chave-secreta"),
        algorithm="HS256"
    )

    return jsonify({"access_token": token})
