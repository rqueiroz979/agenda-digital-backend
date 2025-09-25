from src.extensions import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    razao_social = db.Column(db.String(200), nullable=False)
    nome_fantasia = db.Column(db.String(200), nullable=True)
    cnpj = db.Column(db.String(20), unique=True, nullable=False)
    inscricao_estadual = db.Column(db.String(100), nullable=True)
    inscricao_municipal = db.Column(db.String(100), nullable=True)
    telefone = db.Column(db.String(30), nullable=True)
    whatsapp = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(150), nullable=True)
    endereco = db.Column(db.String(300), nullable=True)
    teamviewer_id = db.Column(db.String(100), nullable=True)
    anydesk_id = db.Column(db.String(100), nullable=True)
    observacoes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'razao_social': self.razao_social,
            'nome_fantasia': self.nome_fantasia,
            'cnpj': self.cnpj,
            'inscricao_estadual': self.inscricao_estadual,
            'inscricao_municipal': self.inscricao_municipal,
            'telefone': self.telefone,
            'whatsapp': self.whatsapp,
            'email': self.email,
            'endereco': self.endereco,
            'teamviewer_id': self.teamviewer_id,
            'anydesk_id': self.anydesk_id,
            'observacoes': self.observacoes
        }
