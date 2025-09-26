import os
from flask import Flask, jsonify
from .extensions import db, migrate, cors
from .routes.auth import auth_bp
from .routes.clientes import clientes_bp

def create_app():
    app = Flask(__name__, static_folder=None)

    # Configurações
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "secret123")
    app.config["JWT_EXP_HOURS"] = int(os.getenv("JWT_EXP_HOURS", "8"))

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # CORS - permite origem definida na env
    allowed = os.getenv("ALLOWED_ORIGINS", "")
    origins = [o.strip() for o in allowed.split(",") if o.strip()]
    if origins:
        cors.init_app(app, resources={r"/*": {"origins": origins}})
    else:
        cors.init_app(app)

    # registrando blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(clientes_bp, url_prefix="/api")

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"})

    return app
