import requests
import re
from typing import Optional, Dict

def consultar_cnpj(cnpj: str) -> Optional[Dict]:
    """
    Consulta dados do CNPJ na API da ReceitaWS
    """
    try:
        # Remove caracteres não numéricos
        cnpj_limpo = re.sub(r'[^0-9]', '', cnpj)
        
        if len(cnpj_limpo) != 14:
            return None
        
        # API gratuita da ReceitaWS
        url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj_limpo}"
        
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('status') == 'OK':
                return {
                    'cnpj': data.get('cnpj'),
                    'razao_social': data.get('nome'),
                    'nome_fantasia': data.get('fantasia'),
                    'endereco': data.get('logradouro'),
                    'numero': data.get('numero'),
                    'complemento': data.get('complemento'),
                    'bairro': data.get('bairro'),
                    'cidade': data.get('municipio'),
                    'uf': data.get('uf'),
                    'cep': data.get('cep'),
                    'telefone1': data.get('telefone'),
                    'email': data.get('email'),
                    'situacao': data.get('situacao'),
                    'atividade_principal': data.get('atividade_principal', [{}])[0].get('text') if data.get('atividade_principal') else None
                }
        
        return None
        
    except requests.RequestException:
        # Em caso de erro na API, retorna None
        return None
    except Exception:
        return None

def consultar_cep(cep: str) -> Optional[Dict]:
    """
    Consulta dados do CEP na API ViaCEP
    """
    try:
        # Remove caracteres não numéricos
        cep_limpo = re.sub(r'[^0-9]', '', cep)
        
        if len(cep_limpo) != 8:
            return None
        
        # API ViaCEP
        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
        
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            # Verifica se não retornou erro
            if not data.get('erro'):
                return {
                    'cep': data.get('cep'),
                    'endereco': data.get('logradouro'),
                    'complemento': data.get('complemento'),
                    'bairro': data.get('bairro'),
                    'cidade': data.get('localidade'),
                    'uf': data.get('uf'),
                    'ibge': data.get('ibge'),
                    'gia': data.get('gia'),
                    'ddd': data.get('ddd'),
                    'siafi': data.get('siafi')
                }
        
        return None
        
    except requests.RequestException:
        # Em caso de erro na API, retorna None
        return None
    except Exception:
        return None

def formatar_cnpj(cnpj: str) -> str:
    """
    Formata CNPJ para exibição (XX.XXX.XXX/XXXX-XX)
    """
    cnpj_limpo = re.sub(r'[^0-9]', '', cnpj)
    if len(cnpj_limpo) == 14:
        return f"{cnpj_limpo[:2]}.{cnpj_limpo[2:5]}.{cnpj_limpo[5:8]}/{cnpj_limpo[8:12]}-{cnpj_limpo[12:]}"
    return cnpj

def formatar_cep(cep: str) -> str:
    """
    Formata CEP para exibição (XXXXX-XXX)
    """
    cep_limpo = re.sub(r'[^0-9]', '', cep)
    if len(cep_limpo) == 8:
        return f"{cep_limpo[:5]}-{cep_limpo[5:]}"
    return cep
