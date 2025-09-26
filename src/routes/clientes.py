from flask import Blueprint, request, jsonify
from src.models import db, Cliente
from sqlalchemy.exc import SQLAlchemyError

clientes_bp = Blueprint("clientes", __name__)

@clientes_bp.route("/clientes", methods=["POST"])
def criar_cliente():
    try:
        data = request.json
        cliente = Cliente(**data)
        db.session.add(cliente)
        db.session.commit()
        return jsonify({"message": "Cliente cadastrado com sucesso!"}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@clientes_bp.route("/clientes", methods=["GET"])
def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([c.to_dict() for c in clientes]), 200

@clientes_bp.route("/clientes/<id>", methods=["GET"])
def obter_cliente(id):
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404
    return jsonify(cliente.to_dict()), 200

@clientes_bp.route("/clientes/<id>", methods=["PUT"])
def atualizar_cliente(id):
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404
    data = request.json
    for key, value in data.items():
        setattr(cliente, key, value)
    db.session.commit()
    return jsonify({"message": "Cliente atualizado com sucesso!"}), 200

@clientes_bp.route("/clientes/<id>", methods=["DELETE"])
def deletar_cliente(id):
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({"message": "Cliente removido com sucesso!"}), 200
