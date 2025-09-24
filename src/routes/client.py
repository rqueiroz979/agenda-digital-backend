from flask import Blueprint, request, jsonify
from src.models.client import Client, db
from datetime import datetime

client_bp = Blueprint('client', __name__)

@client_bp.route('/clients', methods=['GET'])
def get_clients():
    """Obter todos os clientes"""
    try:
        clients = Client.query.all()
        return jsonify([client.to_dict() for client in clients]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@client_bp.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    """Obter um cliente específico"""
    try:
        client = Client.query.get_or_404(client_id)
        return jsonify(client.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@client_bp.route('/clients', methods=['POST'])
def create_client():
    """Criar um novo cliente"""
    try:
        data = request.get_json()
        
        if not data or not data.get('name'):
            return jsonify({'error': 'Nome é obrigatório'}), 400
        
        # Converter string de data para objeto date se fornecido
        last_purchase = None
        if data.get('last_purchase'):
            try:
                last_purchase = datetime.strptime(data.get('last_purchase'), '%Y-%m-%d').date()
            except ValueError:
                return jsonify({'error': 'Formato de data inválido para last_purchase. Use YYYY-MM-DD'}), 400
        
        client = Client(
            name=data.get('name'),
            fantasy_name=data.get('fantasy_name'),
            cnpj_cpf=data.get('cnpj_cpf'),
            email=data.get('email'),
            phone=data.get('phone'),
            phone2=data.get('phone2'),
            mobile=data.get('mobile'),
            cep=data.get('cep'),
            address=data.get('address'),
            number=data.get('number'),
            complement=data.get('complement'),
            neighborhood=data.get('neighborhood'),
            city=data.get('city'),
            state=data.get('state'),
            country=data.get('country', 'Brasil'),
            company=data.get('company'),
            state_registration=data.get('state_registration'),
            municipal_code=data.get('municipal_code'),
            country_code=data.get('country_code', '1058'),
            teamviewer_id=data.get('teamviewer_id'),
            anydesk_id=data.get('anydesk_id'),
            notes=data.get('notes'),
            contact_info=data.get('contact_info'),
            client_group=data.get('client_group'),
            vendor=data.get('vendor'),
            contract_type=data.get('contract_type'),
            payment_type=data.get('payment_type'),
            tax_regime=data.get('tax_regime'),
            monthly_fee=data.get('monthly_fee'),
            last_purchase=last_purchase,
            sale_value=data.get('sale_value')
        )
        
        db.session.add(client)
        db.session.commit()
        
        return jsonify(client.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@client_bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    """Atualizar um cliente"""
    try:
        client = Client.query.get_or_404(client_id)
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400
        
        # Converter string de data para objeto date se fornecido
        if data.get('last_purchase'):
            try:
                data['last_purchase'] = datetime.strptime(data.get('last_purchase'), '%Y-%m-%d').date()
            except ValueError:
                return jsonify({'error': 'Formato de data inválido para last_purchase. Use YYYY-MM-DD'}), 400
        
        # Atualizar campos
        for key, value in data.items():
            if hasattr(client, key):
                setattr(client, key, value)
        
        client.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify(client.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@client_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    """Deletar um cliente"""
    try:
        client = Client.query.get_or_404(client_id)
        db.session.delete(client)
        db.session.commit()
        
        return jsonify({'message': 'Cliente deletado com sucesso'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

