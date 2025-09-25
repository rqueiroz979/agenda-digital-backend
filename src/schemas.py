from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str] = None
    endereco: Optional[str] = None
    telefone: Optional[str] = None
    whatsapp: Optional[str] = None
    email: Optional[str] = None
    teamviewer_id: Optional[str] = None
    anydesk_id: Optional[str] = None
    observacoes: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    id: int

    class Config:
        orm_mode = True
