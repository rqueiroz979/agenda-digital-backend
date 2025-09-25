from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate
from .routes import register_routes
from .config import Config

def create_app():
    """Factory principal da aplicação"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Registra rotas
    register_routes(app)

    return app
