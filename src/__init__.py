from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from src.models import db
from src.routes.auth import auth_bp
from src.routes.clientes import clientes_bp

def create_app():
    app = Flask(__name__)

    # Configuração do banco
    import os
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "secret123")

    # Extensões
    db.init_app(app)
    Migrate(app, db)
    CORS(app)

    # Rotas
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(clientes_bp, url_prefix="/api")

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app
