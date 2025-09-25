from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    CORS(app)

    # Configuração do banco
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "chave-secreta")

    db.init_app(app)
    migrate.init_app(app, db)

    # Importa e registra as rotas
    from src.routes.usuarios import usuarios_bp
    from src.routes.auth import auth_bp

    app.register_blueprint(usuarios_bp, url_prefix="/api/usuarios")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    return app
