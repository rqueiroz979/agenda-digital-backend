# src/models/usuario.py
from datetime import datetime
from src.extensions import db  # usar extensão centralizada
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def set_senha(self, senha: str):
        """Armazena o hash da senha"""
        self.senha_hash = generate_password_hash(senha)

    def check_senha(self, senha: str) -> bool:
        """Verifica senha fornecida contra o hash armazenado"""
        return check_password_hash(self.senha_hash, senha)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "criado_em": self.criado_em.isoformat() if self.criado_em else None,
        }
