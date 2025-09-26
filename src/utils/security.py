import bcrypt
import jwt
import os
from datetime import datetime, timedelta

SECRET_KEY = os.getenv("SECRET_KEY", "secret123")

def gerar_senha_hash(senha):
    return bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verificar_senha(senha, senha_hash):
    return bcrypt.checkpw(senha.encode("utf-8"), senha_hash.encode("utf-8"))

def gerar_token(usuario_id):
    payload = {
        "user_id": usuario_id,
        "exp": datetime.utcnow() + timedelta(hours=8)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
