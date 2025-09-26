from flask import Flask
from flask_cors import CORS
from .models import db
from .routes.auth import auth_bp
from .routes.clientes import clientes_bp


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configuração do banco (será sobrescrita pelo Render)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///agenda.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializa o banco
    db.init_app(app)

    # Registra as rotas
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(clientes_bp, url_prefix="/clientes")

    return app
