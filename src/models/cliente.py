from src import db
from datetime import datetime

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(18), unique=True, nullable=False)
    razao_social = db.Column(db.String(200), nullable=False)
    nome_fantasia = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefone1 = db.Column(db.String(20), nullable=False)
    telefone2 = db.Column(db.String(20))
    endereco = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    inscricao_estadual = db.Column(db.String(50), nullable=False)
    inscricao_municipal = db.Column(db.String(50), nullable=False)
    observacoes = db.Column(db.Text, nullable=False)
    tipo_pagamento = db.Column(db.String(50), nullable=False)
    valor_mensalidade = db.Column(db.Float, nullable=False)
    tipo_contrato = db.Column(db.String(20), nullable=False)  # mensal ou anual
    teamviewer_ids = db.Column(db.ARRAY(db.String), default=[])
    teamviewer_senhas = db.Column(db.ARRAY(db.String), default=[])
    anydesk_ids = db.Column(db.ARRAY(db.String), default=[])
    anydesk_senhas = db.Column(db.ARRAY(db.String), default=[])
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
