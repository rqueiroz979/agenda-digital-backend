# src/models/cliente.py
from datetime import datetime
from src.extensions import db  # usar extensão centralizada

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(18), unique=True, nullable=False)
    razao_social = db.Column(db.String(200), nullable=False)
    nome_fantasia = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefone1 = db.Column(db.String(20), nullable=False)
    telefone2 = db.Column(db.String(20), nullable=True)
    endereco = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    complemento = db.Column(db.String(100), nullable=True)
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    inscricao_estadual = db.Column(db.String(50), nullable=False)
    inscricao_municipal = db.Column(db.String(50), nullable=False)
    observacoes = db.Column(db.Text, nullable=True)
    tipo_pagamento = db.Column(db.String(50), nullable=False)
    valor_mensalidade = db.Column(db.Float, nullable=False)
    tipo_contrato = db.Column(db.String(20), nullable=False)  # mensal ou anual
    # Para arrays (Postgres) você pode usar db.ARRAY; aqui manteremos db.ARRAY
    teamviewer_ids = db.Column(db.ARRAY(db.String), default=[])
    teamviewer_senhas = db.Column(db.ARRAY(db.String), default=[])
    anydesk_ids = db.Column(db.ARRAY(db.String), default=[])
    anydesk_senhas = db.Column(db.ARRAY(db.String), default=[])
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "cnpj": self.cnpj,
            "razao_social": self.razao_social,
            "nome_fantasia": self.nome_fantasia,
            "email": self.email,
            "telefone1": self.telefone1,
            "telefone2": self.telefone2,
            "endereco": self.endereco,
            "numero": self.numero,
            "complemento": self.complemento,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "uf": self.uf,
            "cep": self.cep,
            "inscricao_estadual": self.inscricao_estadual,
            "inscricao_municipal": self.inscricao_municipal,
            "observacoes": self.observacoes,
            "tipo_pagamento": self.tipo_pagamento,
            "valor_mensalidade": self.valor_mensalidade,
            "tipo_contrato": self.tipo_contrato,
            "teamviewer_ids": self.teamviewer_ids,
            "teamviewer_senhas": self.teamviewer_senhas,
            "anydesk_ids": self.anydesk_ids,
            "anydesk_senhas": self.anydesk_senhas,
            "criado_em": self.criado_em.isoformat() if self.criado_em else None,
        }
