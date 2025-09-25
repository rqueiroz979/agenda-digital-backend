from flask import Blueprint, request, jsonify
from src import db
from src.models.usuario import Usuario
from werkzeug.security import generate_password_hash

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/", methods=["POST"])
def criar_usuario():
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")

    if not nome or not email or not senha:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    # Verifica se já existe
    if Usuario.query.filter_by(email=email).first():
        return jsonify({"error": "E-mail já cadastrado"}), 400

    novo_usuario = Usuario(
        nome=nome,
        email=email,
        senha=generate_password_hash(senha)
    )

    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"message": "Usuário criado com sucesso"}), 201


@usuarios_bp.route("/", methods=["GET"])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios])
