from flask import Blueprint, request, jsonify
from services.external_apis import ExternalAPIService

external_apis_bp = Blueprint('external_apis', __name__)
api_service = ExternalAPIService()

@external_apis_bp.route('/consultar-cnpj/<cnpj>', methods=['GET'])
def consultar_cnpj(cnpj):
    """Consultar dados de CNPJ"""
    try:
        result = api_service.consultar_cnpj(cnpj)
        return jsonify(result), 200 if result['success'] else 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@external_apis_bp.route('/consultar-cep/<cep>', methods=['GET'])
def consultar_cep(cep):
    """Consultar dados de CEP"""
    try:
        result = api_service.consultar_cep(cep)
        return jsonify(result), 200 if result['success'] else 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@external_apis_bp.route('/whatsapp-link', methods=['POST'])
def gerar_link_whatsapp():
    """Gerar link do WhatsApp"""
    try:
        data = request.get_json()
        
        if not data or not data.get('phone'):
            return jsonify({'error': 'Telefone é obrigatório'}), 400
        
        phone = data.get('phone')
        message = data.get('message', '')
        
        link = api_service.gerar_link_whatsapp(phone, message)
        
        return jsonify({
            'success': True,
            'link': link
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

