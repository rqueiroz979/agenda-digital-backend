
import os
import sys
from functools import wraps

# Permite importar src/... mesmo quando rodando no Render / local
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request, jsonify, g, send_from_directory
from flask_cors import CORS
import jwt
import datetime

from extensions import db, migrate

from src.models.client import Cliente
from src.config import Config

# ---------------------
# Decorator de autenticação JWT (importável por outras rotas)
# ---------------------
def token_required(f):
    """
    Decorator para proteger rotas com JWT.
    Uso nas rotas: from main import token_required
    @token_required
    def rota_protegida(): ...
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        auth_header = request.headers.get("Authorization", None)
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ", 1)[1]

        if not token:
            return jsonify({"error": "Token é necessário"}), 401

        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("user_id")
            from src.models.user import User

            user = User.query.get(user_id)

            if not user:

                return jsonify({"error": "Usuário não encontrado"}), 401
            g.current_user = user
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}), 401
        except Exception as e:
            return jsonify({"error": "Token inválido", "detail": str(e)}), 401

        return f(*args, **kwargs)
    return decorator

# ---------------------
# Factory simples de app
# ---------------------
def create_app():
    app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), "static"))
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    CORS(app, origins="*", allow_headers=["Content-Type", "Authorization"], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

    with app.app_context():
        try:
            from src.routes.user import user_bp
            from src.routes.client import client_bp
            try:
                from src.routes.external_apis import external_apis_bp
            except Exception:
                external_apis_bp = None
        except Exception as e:
            raise RuntimeError(f"Erro ao importar blueprints: {e}")

        app.register_blueprint(user_bp, url_prefix="/api/usuarios")
        app.register_blueprint(client_bp, url_prefix="/api/clientes")
        if external_apis_bp:
            app.register_blueprint(external_apis_bp, url_prefix="/api/external")

    @app.route("/health")
    def health():
        return {"status": "ok"}

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def serve(path):
        static_folder_path = app.static_folder
        if static_folder_path is None:
            return "Static folder not configured", 404

        full_path = os.path.join(static_folder_path, path)
        if path != "" and os.path.exists(full_path):
            return send_from_directory(static_folder_path, path)
        index_path = os.path.join(static_folder_path, "index.html")
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, "index.html")
        return "index.html not found", 404

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)


