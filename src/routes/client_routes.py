from flask import Blueprint, request, jsonify
from src.extensions import db
from src.models.client import Cliente
from src.auth import token_required

client_bp = Blueprint('client_bp', __name__)

@client_bp.route('/', methods=['GET'])
@token_required
def list_clients():
    clients = Cliente.query.all()
    return jsonify([c.to_dict() for c in clients])

@client_bp.route('/', methods=['POST'])
@token_required
def create_client():
    data = request.get_json() or {}
    required = ['cnpj', 'razao_social']
    for r in required:
        if not data.get(r):
            return jsonify({'msg': f'{r} obrigatório'}), 400
    if Cliente.query.filter_by(cnpj=data['cnpj']).first():
        return jsonify({'msg': 'CNPJ já cadastrado'}), 400
    c = Cliente(
        razao_social=data.get('razao_social'),
        nome_fantasia=data.get('nome_fantasia'),
        cnpj=data.get('cnpj'),
        inscricao_estadual=data.get('inscricao_estadual'),
        inscricao_municipal=data.get('inscricao_municipal'),
        telefone=data.get('telefone'),
        whatsapp=data.get('whatsapp'),
        email=data.get('email'),
        endereco=data.get('endereco'),
        teamviewer_id=data.get('teamviewer_id'),
        anydesk_id=data.get('anydesk_id'),
        observacoes=data.get('observacoes')
    )
    db.session.add(c)
    db.session.commit()
    return jsonify({'msg': 'Cliente criado', 'cliente': c.to_dict()}), 201

@client_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_client(id):
    c = Cliente.query.get_or_404(id)
    return jsonify(c.to_dict())

@client_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_client(id):
    c = Cliente.query.get_or_404(id)
    data = request.get_json() or {}
    for key, val in data.items():
        if hasattr(c, key):
            setattr(c, key, val)
    db.session.commit()
    return jsonify({'msg': 'Atualizado', 'cliente': c.to_dict()})

@client_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_client(id):
    c = Cliente.query.get_or_404(id)
    db.session.delete(c)
    db.session.commit()
    return jsonify({'msg': 'Removido'})
