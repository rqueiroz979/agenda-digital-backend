from flask import Blueprint, request, jsonify
from src.extensions import db
from src.models.client import Cliente
from src.utils.external_lookups import consultar_cnpj, consultar_cep
from sqlalchemy.exc import SQLAlchemyError
import re

clientes_bp = Blueprint("clientes", __name__)

def validar_cnpj(cnpj):
    """Valida formato do CNPJ"""
    cnpj = re.sub(r'[^0-9]', '', cnpj)
    return len(cnpj) == 14

def validar_cep(cep):
    """Valida formato do CEP"""
    cep = re.sub(r'[^0-9]', '', cep)
    return len(cep) == 8

@clientes_bp.route("/clientes", methods=["POST"])
def criar_cliente():
    try:
        data = request.json
        
        # Validações básicas
        if not data.get('cnpj'):
            return jsonify({"error": "CNPJ é obrigatório"}), 400
        
        if not validar_cnpj(data['cnpj']):
            return jsonify({"error": "CNPJ inválido"}), 400
        
        if not data.get('razao_social'):
            return jsonify({"error": "Razão Social é obrigatória"}), 400
        
        # Verifica se CNPJ já existe
        cnpj_limpo = re.sub(r'[^0-9]', '', data['cnpj'])
        if Cliente.query.filter_by(cnpj=cnpj_limpo).first():
            return jsonify({"error": "CNPJ já cadastrado"}), 400
        
        # Processa IDs de TeamViewer e AnyDesk
        teamviewer_ids = data.get('teamviewer_ids', [])
        anydesk_ids = data.get('anydesk_ids', [])
        
        # Limita a 6 IDs cada
        if len(teamviewer_ids) > 6:
            return jsonify({"error": "Máximo de 6 IDs TeamViewer permitidos"}), 400
        
        if len(anydesk_ids) > 6:
            return jsonify({"error": "Máximo de 6 IDs AnyDesk permitidos"}), 400
        
        # Cria o cliente
        cliente = Cliente(
            cnpj=cnpj_limpo,
            razao_social=data.get('razao_social'),
            nome_fantasia=data.get('nome_fantasia'),
            cep=data.get('cep'),
            endereco=data.get('endereco'),
            numero=data.get('numero'),
            complemento=data.get('complemento'),
            bairro=data.get('bairro'),
            cidade=data.get('cidade'),
            uf=data.get('uf'),
            telefone1=data.get('telefone1'),
            telefone2=data.get('telefone2'),
            email=data.get('email'),
            inscricao_estadual=data.get('inscricao_estadual'),
            inscricao_municipal=data.get('inscricao_municipal'),
            tipo_pagamento=data.get('tipo_pagamento'),
            valor_mensalidade=data.get('valor_mensalidade'),
            tipo_contrato=data.get('tipo_contrato'),
            observacoes=data.get('observacoes')
        )
        
        # Define os IDs de acesso remoto
        cliente.set_teamviewer_ids(teamviewer_ids)
        cliente.set_anydesk_ids(anydesk_ids)
        
        db.session.add(cliente)
        db.session.commit()
        
        return jsonify({
            "message": "Cliente cadastrado com sucesso!",
            "cliente": cliente.to_dict()
        }), 201
        
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": f"Erro no banco de dados: {str(e)}"}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500

@clientes_bp.route("/clientes", methods=["GET"])
def listar_clientes():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        search = request.args.get('search', '')
        
        query = Cliente.query
        
        if search:
            query = query.filter(
                db.or_(
                    Cliente.razao_social.ilike(f'%{search}%'),
                    Cliente.nome_fantasia.ilike(f'%{search}%'),
                    Cliente.cnpj.ilike(f'%{search}%')
                )
            )
        
        clientes = query.paginate(
            page=page, 
            per_page=per_page, 
            error_out=False
        )
        
        return jsonify({
            "clientes": [c.to_dict() for c in clientes.items],
            "total": clientes.total,
            "pages": clientes.pages,
            "current_page": page
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Erro ao listar clientes: {str(e)}"}), 500

@clientes_bp.route("/clientes/<int:id>", methods=["GET"])
def obter_cliente(id):
    try:
        cliente = Cliente.query.get(id)
        if not cliente:
            return jsonify({"error": "Cliente não encontrado"}), 404
        return jsonify(cliente.to_dict()), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao obter cliente: {str(e)}"}), 500

@clientes_bp.route("/clientes/<int:id>", methods=["PUT"])
def atualizar_cliente(id):
    try:
        cliente = Cliente.query.get(id)
        if not cliente:
            return jsonify({"error": "Cliente não encontrado"}), 404
        
        data = request.json
        
        # Validações se CNPJ foi alterado
        if 'cnpj' in data and data['cnpj'] != cliente.cnpj:
            if not validar_cnpj(data['cnpj']):
                return jsonify({"error": "CNPJ inválido"}), 400
            
            cnpj_limpo = re.sub(r'[^0-9]', '', data['cnpj'])
            if Cliente.query.filter(Cliente.cnpj == cnpj_limpo, Cliente.id != id).first():
                return jsonify({"error": "CNPJ já cadastrado"}), 400
            data['cnpj'] = cnpj_limpo
        
        # Processa IDs de acesso remoto
        if 'teamviewer_ids' in data:
            if len(data['teamviewer_ids']) > 6:
                return jsonify({"error": "Máximo de 6 IDs TeamViewer permitidos"}), 400
            cliente.set_teamviewer_ids(data['teamviewer_ids'])
            del data['teamviewer_ids']
        
        if 'anydesk_ids' in data:
            if len(data['anydesk_ids']) > 6:
                return jsonify({"error": "Máximo de 6 IDs AnyDesk permitidos"}), 400
            cliente.set_anydesk_ids(data['anydesk_ids'])
            del data['anydesk_ids']
        
        # Atualiza outros campos
        for key, value in data.items():
            if hasattr(cliente, key):
                setattr(cliente, key, value)
        
        db.session.commit()
        return jsonify({
            "message": "Cliente atualizado com sucesso!",
            "cliente": cliente.to_dict()
        }), 200
        
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": f"Erro no banco de dados: {str(e)}"}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500

@clientes_bp.route("/clientes/<int:id>", methods=["DELETE"])
def deletar_cliente(id):
    try:
        cliente = Cliente.query.get(id)
        if not cliente:
            return jsonify({"error": "Cliente não encontrado"}), 404
        
        db.session.delete(cliente)
        db.session.commit()
        return jsonify({"message": "Cliente removido com sucesso!"}), 200
        
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": f"Erro no banco de dados: {str(e)}"}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500

@clientes_bp.route("/consultar-cnpj/<cnpj>", methods=["GET"])
def consultar_cnpj_route(cnpj):
    try:
        if not validar_cnpj(cnpj):
            return jsonify({"error": "CNPJ inválido"}), 400
        
        dados = consultar_cnpj(cnpj)
        if dados:
            return jsonify(dados), 200
        else:
            return jsonify({"error": "CNPJ não encontrado"}), 404
            
    except Exception as e:
        return jsonify({"error": f"Erro ao consultar CNPJ: {str(e)}"}), 500

@clientes_bp.route("/consultar-cep/<cep>", methods=["GET"])
def consultar_cep_route(cep):
    try:
        if not validar_cep(cep):
            return jsonify({"error": "CEP inválido"}), 400
        
        dados = consultar_cep(cep)
        if dados:
            return jsonify(dados), 200
        else:
            return jsonify({"error": "CEP não encontrado"}), 404
            
    except Exception as e:
        return jsonify({"error": f"Erro ao consultar CEP: {str(e)}"}), 500

