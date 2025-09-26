from flask import Flask, jsonify
from flask_cors import CORS
from extensions import db, migrate
from routes.auth_routes import auth_bp
from routes.usuario_routes import usuario_bp
from routes.cliente_routes import cliente_bp
import os

app = Flask(__name__)

# Configuração
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar extensões
db.init_app(app)
migrate.init_app(app, db)

# Configurar CORS (para localhost e Netlify)
CORS(app, resources={r"/*": {"origins": [
    "http://localhost:5173",
    "https://agenda-digital-frontend.netlify.app"
]}})

# Rotas
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(usuario_bp, url_prefix="/api/usuarios")
app.register_blueprint(cliente_bp, url_prefix="/api/clientes")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
