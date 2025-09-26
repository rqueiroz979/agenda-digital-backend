import os
import bcrypt
import jwt
from datetime import datetime, timedelta
from flask import current_app

SECRET_KEY = lambda: os.getenv("SECRET_KEY", current_app.config.get("SECRET_KEY", "secret123"))

def gerar_senha_hash(senha: str) -> str:
    return bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verificar_senha(senha: str, senha_hash: str) -> bool:
    return bcrypt.checkpw(senha.encode("utf-8"), senha_hash.encode("utf-8"))

def gerar_token(user_id: str) -> str:
    exp = datetime.utcnow() + timedelta(hours=int(current_app.config.get("JWT_EXP_HOURS", 8)))
    payload = {"user_id": user_id, "exp": exp.timestamp()}
    token = jwt.encode(payload, SECRET_KEY(), algorithm="HS256")
    # PyJWT v2 retorna str
    return token

def decodificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY(), algorithms=["HS256"])
        return payload
    except Exception:
        return None
