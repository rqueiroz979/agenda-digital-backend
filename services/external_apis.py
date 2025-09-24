"""
Serviços para integração com APIs externas
"""
import requests
import re
from urllib.parse import quote


class ExternalAPIService:
    """Serviço para integração com APIs externas"""
    
    def __init__(self):
        self.timeout = 10
    
    def clean_cnpj(self, cnpj):
        """Remove caracteres especiais do CNPJ"""
        return re.sub(r'[^0-9]', '', cnpj)
    
    def clean_cep(self, cep):
        """Remove caracteres especiais do CEP"""
        return re.sub(r'[^0-9]', '', cep)
    
    def format_phone_for_whatsapp(self, phone):
        """Formata telefone para WhatsApp (apenas números)"""
        phone_clean = re.sub(r'[^0-9]', '', phone)
        
        # Se não tem código do país, adiciona 55 (Brasil)
        if len(phone_clean) == 11 and phone_clean.startswith('0'):
            phone_clean = '55' + phone_clean[1:]
        elif len(phone_clean) == 10:
            phone_clean = '55' + phone_clean
        elif len(phone_clean) == 11 and not phone_clean.startswith('55'):
            phone_clean = '55' + phone_clean
        
        return phone_clean
    
    def consultar_cnpj(self, cnpj):
        """Consulta dados de CNPJ usando BrasilAPI"""
        try:
            cnpj_clean = self.clean_cnpj(cnpj)
            
            if len(cnpj_clean) != 14:
                return {
                    'success': False,
                    'error': 'CNPJ deve conter 14 dígitos'
                }
            
            url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_clean}"
            
            response = requests.get(url, timeout=self.timeout)
            
            if response.status_code == 200:
                data = response.json()
                
                # Mapear dados da BrasilAPI para nosso formato
                result = {
                    'cnpj': data.get('cnpj', ''),
                    'razao_social': data.get('company_name', ''),
                    'nome_fantasia': data.get('trade_name', ''),
                    'telefone': data.get('phone', ''),
                    'email': data.get('email', ''),
                    'cep': data.get('zip_code', ''),
                    'logradouro': data.get('street', ''),
                    'numero': data.get('number', ''),
                    'complemento': data.get('complement', ''),
                    'bairro': data.get('district', ''),
                    'municipio': data.get('city', ''),
                    'uf': data.get('state', ''),
                    'situacao': data.get('status', ''),
                    'atividade_principal': data.get('main_activity', {}).get('text', '') if data.get('main_activity') else ''
                }
                
                return {
                    'success': True,
                    'data': result
                }
            elif response.status_code == 404:
                return {
                    'success': False,
                    'error': 'CNPJ não encontrado'
                }
            else:
                return {
                    'success': False,
                    'error': f'Erro na consulta: {response.status_code}'
                }
                
        except requests.exceptions.Timeout:
            return {
                'success': False,
                'error': 'Timeout na consulta do CNPJ'
            }
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': f'Erro na requisição: {str(e)}'
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Erro interno: {str(e)}'
            }
    
    def consultar_cep(self, cep):
        """Consulta dados de CEP usando ViaCEP"""
        try:
            cep_clean = self.clean_cep(cep)
            
            if len(cep_clean) != 8:
                return {
                    'success': False,
                    'error': 'CEP deve conter 8 dígitos'
                }
            
            url = f"https://viacep.com.br/ws/{cep_clean}/json/"
            
            response = requests.get(url, timeout=self.timeout)
            
            if response.status_code == 200:
                data = response.json()
                
                if 'erro' in data:
                    return {
                        'success': False,
                        'error': 'CEP não encontrado'
                    }
                
                result = {
                    'cep': data.get('cep', ''),
                    'logradouro': data.get('logradouro', ''),
                    'complemento': data.get('complemento', ''),
                    'bairro': data.get('bairro', ''),
                    'localidade': data.get('localidade', ''),
                    'uf': data.get('uf', ''),
                    'ibge': data.get('ibge', ''),
                    'gia': data.get('gia', ''),
                    'ddd': data.get('ddd', ''),
                    'siafi': data.get('siafi', '')
                }
                
                return {
                    'success': True,
                    'data': result
                }
            else:
                return {
                    'success': False,
                    'error': f'Erro na consulta: {response.status_code}'
                }
                
        except requests.exceptions.Timeout:
            return {
                'success': False,
                'error': 'Timeout na consulta do CEP'
            }
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'error': f'Erro na requisição: {str(e)}'
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Erro interno: {str(e)}'
            }
    
    def gerar_link_whatsapp(self, phone, message=''):
        """Gera link do WhatsApp para um número"""
        try:
            phone_formatted = self.format_phone_for_whatsapp(phone)
            
            if message:
                message_encoded = quote(message)
                return f"https://wa.me/{phone_formatted}?text={message_encoded}"
            else:
                return f"https://wa.me/{phone_formatted}"
                
        except Exception as e:
            return f"https://wa.me/{phone}"

