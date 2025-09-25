from main import db

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Identificação
    cnpj = db.Column(db.String(20), nullable=False, unique=True)
    razao_social = db.Column(db.String(255), nullable=False)
    nome_fantasia = db.Column(db.String(255), nullable=True)

    # Inscrições
    inscricao_estadual = db.Column(db.String(50), nullable=True)
    inscricao_municipal = db.Column(db.String(50), nullable=True)

    # Contatos
    telefone = db.Column(db.String(20), nullable=True)
    whatsapp = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(255), nullable=True)

    # Endereço
    endereco = db.Column(db.Text, nullable=True)

    # Acesso remoto
    teamviewer_id = db.Column(db.String(50), nullable=True)
    anydesk_id = db.Column(db.String(50), nullable=True)

    # Observações
    observacoes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Cliente {self.razao_social} - {self.cnpj}>"
