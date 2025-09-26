# src/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# Extensões globais
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def init_extensions(app):
    """Inicializa todas as extensões Flask no app."""
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    jwt.init_app(app)
