from flask import Blueprint, request, jsonify
from src.models import db, Usuario
from src.utils.security import gerar_senha_hash, verificar_senha, gerar_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if Usuario.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "E-mail já cadastrado"}), 400

    senha_hash = gerar_senha_hash(data["senha"])
    usuario = Usuario(nome=data["nome"], email=data["email"], senha=senha_hash)
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    usuario = Usuario.query.filter_by(email=data["email"]).first()
    if not usuario or not verificar_senha(data["senha"], usuario.senha):
        return jsonify({"error": "Credenciais inválidas"}), 401

    token = gerar_token(usuario.id)
    return jsonify({"token": token, "usuario": usuario.to_dict()}), 200
