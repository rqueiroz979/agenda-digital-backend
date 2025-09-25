from sqlalchemy import Column, Integer, String, Text
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String, nullable=False)
    razao_social = Column(String, nullable=False)
    nome_fantasia = Column(String)
    endereco = Column(Text)
    telefone = Column(String)
    whatsapp = Column(String)
    email = Column(String)
    teamviewer_id = Column(String)
    anydesk_id = Column(String)
    observacoes = Column(Text)
