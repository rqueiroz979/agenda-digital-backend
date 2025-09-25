from flask import Blueprint, request, jsonify
from main import db
from src.models.client import Cliente

client_bp = Blueprint("client", __name__)

# Criar cliente
@client_bp.route("/", methods=["POST"])
def criar_cliente():
    data = request.get_json()

    try:
        novo_cliente = Cliente(
            cnpj=data.get("cnpj"),
            razao_social=data.get("razao_social"),
            nome_fantasia=data.get("nome_fantasia"),
            inscricao_estadual=data.get("inscricao_estadual"),
            inscricao_municipal=data.get("inscricao_municipal"),
            telefone=data.get("telefone"),
            whatsapp=data.get("whatsapp"),
            email=data.get("email"),
            endereco=data.get("endereco"),
            teamviewer_id=data.get("teamviewer_id"),
            anydesk_id=data.get("anydesk_id"),
            observacoes=data.get("observacoes"),
        )
        db.session.add(novo_cliente)
        db.session.commit()

        return jsonify({"msg": "✅ Cliente criado com sucesso!", "id": novo_cliente.id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


# Listar todos os clientes
@client_bp.route("/", methods=["GET"])
def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([
        {
            "id": c.id,
            "cnpj": c.cnpj,
            "razao_social": c.razao_social,
            "nome_fantasia": c.nome_fantasia,
            "inscricao_estadual": c.inscricao_estadual,
            "inscricao_municipal": c.inscricao_municipal,
            "telefone": c.telefone,
            "whatsapp": c.whatsapp,
            "email": c.email,
            "endereco": c.endereco,
            "teamviewer_id": c.teamviewer_id,
            "anydesk_id": c.anydesk_id,
            "observacoes": c.observacoes,
        }
        for c in clientes
    ])


# Buscar cliente por ID
@client_bp.route("/<int:cliente_id>", methods=["GET"])
def obter_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404

    return jsonify({
        "id": cliente.id,
        "cnpj": cliente.cnpj,
        "razao_social": cliente.razao_social,
        "nome_fantasia": cliente.nome_fantasia,
        "inscricao_estadual": cliente.inscricao_estadual,
        "inscricao_municipal": cliente.inscricao_municipal,
        "telefone": cliente.telefone,
        "whatsapp": cliente.whatsapp,
        "email": cliente.email,
        "endereco": cliente.endereco,
        "teamviewer_id": cliente.teamviewer_id,
        "anydesk_id": cliente.anydesk_id,
        "observacoes": cliente.observacoes,
    })


# Atualizar cliente
@client_bp.route("/<int:cliente_id>", methods=["PUT"])
def atualizar_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404

    data = request.get_json()
    try:
        cliente.cnpj = data.get("cnpj", cliente.cnpj)
        cliente.razao_social = data.get("razao_social", cliente.razao_social)
        cliente.nome_fantasia = data.get("nome_fantasia", cliente.nome_fantasia)
        cliente.inscricao_estadual = data.get("inscricao_estadual", cliente.inscricao_estadual)
        cliente.inscricao_municipal = data.get("inscricao_municipal", cliente.inscricao_municipal)
        cliente.telefone = data.get("telefone", cliente.telefone)
        cliente.whatsapp = data.get("whatsapp", cliente.whatsapp)
        cliente.email = data.get("email", cliente.email)
        cliente.endereco = data.get("endereco", cliente.endereco)
        cliente.teamviewer_id = data.get("teamviewer_id", cliente.teamviewer_id)
        cliente.anydesk_id = data.get("anydesk_id", cliente.anydesk_id)
        cliente.observacoes = data.get("observacoes", cliente.observacoes)

        db.session.commit()
        return jsonify({"msg": "✅ Cliente atualizado com sucesso!"})

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


# Deletar cliente
@client_bp.route("/<int:cliente_id>", methods=["DELETE"])
def deletar_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404

    try:
        db.session.delete(cliente)
        db.session.commit()
        return jsonify({"msg": "🗑️ Cliente deletado com sucesso!"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
