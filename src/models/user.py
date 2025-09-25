from src.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, raw):
        self.senha = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self.senha, raw)

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'email': self.email}
