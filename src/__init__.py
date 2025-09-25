from flask import Flask, jsonify
from flask_cors import CORS
from .extensions import db, migrate
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # health
    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})

    # register blueprints under /api
    from .routes.user_routes import user_bp
    from .routes.client_routes import client_bp

    app.register_blueprint(user_bp, url_prefix="/api/usuarios")
    app.register_blueprint(client_bp, url_prefix="/api/clientes")

    return app
