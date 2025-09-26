from src.extensions import db
import json

class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    # Campos básicos
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(20), unique=True, nullable=False)
    razao_social = db.Column(db.String(200), nullable=False)
    nome_fantasia = db.Column(db.String(200), nullable=True)
    
    # Endereço
    cep = db.Column(db.String(10), nullable=True)
    endereco = db.Column(db.String(300), nullable=True)
    numero = db.Column(db.String(20), nullable=True)
    complemento = db.Column(db.String(100), nullable=True)
    bairro = db.Column(db.String(100), nullable=True)
    cidade = db.Column(db.String(100), nullable=True)
    uf = db.Column(db.String(2), nullable=True)
    
    # Contatos
    telefone1 = db.Column(db.String(30), nullable=True)
    telefone2 = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(150), nullable=True)
    
    # Documentos
    inscricao_estadual = db.Column(db.String(100), nullable=True)
    inscricao_municipal = db.Column(db.String(100), nullable=True)
    
    # Financeiro
    tipo_pagamento = db.Column(db.String(50), nullable=True)
    valor_mensalidade = db.Column(db.Numeric(10, 2), nullable=True)
    tipo_contrato = db.Column(db.String(20), nullable=True)  # Mensal/Anual
    
    # Acessos remotos (JSON)
    teamviewer_ids = db.Column(db.Text, nullable=True)  # JSON array
    anydesk_ids = db.Column(db.Text, nullable=True)     # JSON array
    
    # Observações
    observacoes = db.Column(db.Text, nullable=True)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def set_teamviewer_ids(self, ids_list):
        """Define os IDs do TeamViewer como JSON"""
        self.teamviewer_ids = json.dumps(ids_list) if ids_list else None

    def get_teamviewer_ids(self):
        """Retorna os IDs do TeamViewer como lista"""
        return json.loads(self.teamviewer_ids) if self.teamviewer_ids else []

    def set_anydesk_ids(self, ids_list):
        """Define os IDs do AnyDesk como JSON"""
        self.anydesk_ids = json.dumps(ids_list) if ids_list else None

    def get_anydesk_ids(self):
        """Retorna os IDs do AnyDesk como lista"""
        return json.loads(self.anydesk_ids) if self.anydesk_ids else []

    def to_dict(self):
        return {
            'id': self.id,
            'cnpj': self.cnpj,
            'razao_social': self.razao_social,
            'nome_fantasia': self.nome_fantasia,
            'cep': self.cep,
            'endereco': self.endereco,
            'numero': self.numero,
            'complemento': self.complemento,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'uf': self.uf,
            'telefone1': self.telefone1,
            'telefone2': self.telefone2,
            'email': self.email,
            'inscricao_estadual': self.inscricao_estadual,
            'inscricao_municipal': self.inscricao_municipal,
            'tipo_pagamento': self.tipo_pagamento,
            'valor_mensalidade': float(self.valor_mensalidade) if self.valor_mensalidade else None,
            'tipo_contrato': self.tipo_contrato,
            'teamviewer_ids': self.get_teamviewer_ids(),
            'anydesk_ids': self.get_anydesk_ids(),
            'observacoes': self.observacoes,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

