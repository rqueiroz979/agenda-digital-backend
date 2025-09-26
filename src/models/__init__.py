# src/models/__init__.py
# Registro dos models do pacote

from src.extensions import db  # pegue db do módulo de extensões
# importar classes localmente (evita importações circulares se feitas corretamente)
from .usuario import Usuario
from .cliente import Cliente

__all__ = ["db", "Usuario", "Cliente"]
