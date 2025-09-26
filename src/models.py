from .extensions import db
import uuid

def gen_uuid():
    return str(uuid.uuid4())

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.String, primary_key=True, default=gen_uuid)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    senha_hash = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}

class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.String, primary_key=True, default=gen_uuid)
    cnpj = db.Column(db.String(18), nullable=False)
    razao_social = db.Column(db.Text, nullable=False)
    nome_fantasia = db.Column(db.Text, nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    endereco = db.Column(db.Text, nullable=False)
    numero = db.Column(db.Text, nullable=False)
    complemento = db.Column(db.Text, nullable=False)
    bairro = db.Column(db.Text, nullable=False)
    cidade = db.Column(db.Text, nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    telefone1 = db.Column(db.String(20), nullable=False)
    telefone2 = db.Column(db.String(20))
    email = db.Column(db.Text, nullable=False)
    inscricao_estadual = db.Column(db.Text, nullable=False)
    inscricao_municipal = db.Column(db.Text, nullable=False)
    observacoes = db.Column(db.Text, nullable=False)
    tipo_pagamento = db.Column(db.Text, nullable=False)
    valor_mensalidade = db.Column(db.Numeric(10,2), nullable=False)
    tipo_contrato = db.Column(db.Text, nullable=False)

    # teamviewer (até 6)
    teamviewer1 = db.Column(db.Text); teamviewer1_senha = db.Column(db.Text)
    teamviewer2 = db.Column(db.Text); teamviewer2_senha = db.Column(db.Text)
    teamviewer3 = db.Column(db.Text); teamviewer3_senha = db.Column(db.Text)
    teamviewer4 = db.Column(db.Text); teamviewer4_senha = db.Column(db.Text)
    teamviewer5 = db.Column(db.Text); teamviewer5_senha = db.Column(db.Text)
    teamviewer6 = db.Column(db.Text); teamviewer6_senha = db.Column(db.Text)

    # anydesk (até 6)
    anydesk1 = db.Column(db.Text); anydesk1_senha = db.Column(db.Text)
    anydesk2 = db.Column(db.Text); anydesk2_senha = db.Column(db.Text)
    anydesk3 = db.Column(db.Text); anydesk3_senha = db.Column(db.Text)
    anydesk4 = db.Column(db.Text); anydesk4_senha = db.Column(db.Text)
    anydesk5 = db.Column(db.Text); anydesk5_senha = db.Column(db.Text)
    anydesk6 = db.Column(db.Text); anydesk6_senha = db.Column(db.Text)

    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
