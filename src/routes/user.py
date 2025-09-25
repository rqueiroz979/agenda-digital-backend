from flask import Blueprint, request, jsonify
from main import db, SECRET_KEY
from src.models.user import User
import jwt, datetime

user_bp = Blueprint("user", __name__)

# Criar usuário (cadastro)
@user_bp.route("/", methods=["POST"])
def criar_usuario():
    data = request.get_json()

    if not data.get("email") or not data.get("senha"):
        return jsonify({"error": "Email e senha são obrigatórios"}), 400

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Usuário já existe"}), 400

    novo_user = User(
        nome=data.get("nome"),
        email=data["email"]
    )
    novo_user.set_password(data["senha"])

    db.session.add(novo_user)
    db.session.commit()

    return jsonify({"msg": "✅ Usuário criado com sucesso!"}), 201


# Login
@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data.get("email") or not data.get("senha"):
        return jsonify({"error": "Email e senha são obrigatórios"}), 400

    user = User.query.filter_by(email=data.get("email")).first()

    if not user or not user.check_password(data.get("senha")):
        return jsonify({"error": "Credenciais inválidas"}), 401

    token = jwt.encode(
        {
            "user_id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8)  # expira em 8 horas
        },
        SECRET_KEY,
        algorithm="HS256"
    )

    return jsonify({"token": token, "user": {"id": user.id, "nome": user.nome, "email": user.email}})
