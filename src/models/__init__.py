from flask_sqlalchemy import SQLAlchemy

# Instância global do banco
db = SQLAlchemy()

# Importa os modelos
from .usuario import Usuario
from .cliente import Cliente

__all__ = ["db", "Usuario", "Cliente"]
