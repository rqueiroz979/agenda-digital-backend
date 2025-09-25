from src import create_app
from src.extensions import db, migrate

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, jsonify
from src import create_app, db

app = create_app()

# Rota raiz para não dar 404
@app.route("/")
def index():
    return jsonify({"message": "API da Agenda Digital está rodando 🚀"})


@app.route("/api/")
def api_index():
    return jsonify({"message": "Bem-vindo à API da Agenda Digital"})


# Healthcheck (Render usa para validar se está no ar)
@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
