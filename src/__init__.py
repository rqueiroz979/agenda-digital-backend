# src/__init__.py
from flask import Flask
from src.extensions import init_extensions, db
from src.routes.auth import auth_bp
from src.routes.clientes import clientes_bp

def create_app():
    app = Flask(__name__)

    # Configurações básicas
    app.config.from_mapping(
        SECRET_KEY="supersecretkey",  # substitua por variável de ambiente no Render
        SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://usuario:senha@host:5432/db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        JWT_SECRET_KEY="jwtsecret",  # também use variável de ambiente
    )

    # Inicializar extensões
    init_extensions(app)

    # Registrar blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(clientes_bp, url_prefix="/clientes")

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app
