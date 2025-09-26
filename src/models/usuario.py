from src import db, bcrypt
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, senha):
        self.senha_hash = bcrypt.generate_password_hash(senha).decode("utf-8")

    def check_password(self, senha):
        return bcrypt.check_password_hash(self.senha_hash, senha)
