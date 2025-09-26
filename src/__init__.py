from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    load_dotenv()

    app = Flask(__name__)

    # Configurações do banco
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Importa os modelos para o Alembic reconhecer
    from src import models

    # Importa rotas
    from src.routes.auth import auth_bp
    from src.routes.clientes import clientes_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(clientes_bp, url_prefix="/clientes")

    return app
