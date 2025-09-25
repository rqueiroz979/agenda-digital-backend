import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret-change-me")
    DATABASE_URL = os.getenv("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = DATABASE_URL.replace("postgres://", "postgresql://", 1) if DATABASE_URL and DATABASE_URL.startswith("postgres://") else DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 8 * 60 * 60) # 8 horas em segundos

    if not DATABASE_URL:
        raise RuntimeError("❌ Variável de ambiente DATABASE_URL não configurada!")


