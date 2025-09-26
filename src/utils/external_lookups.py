import requests
import os

TIMEOUT = int(os.getenv("EXTERNAL_API_TIMEOUT", "8"))

def buscar_cnpj_receitaws(cnpj: str) -> dict:
    """Consulta receita.ws (receitaws.com.br) - note que tem limite de uso público.
      
