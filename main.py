from src import create_app

# cria a app e expõe a variável app (necessário pelo gunicorn: main:app)
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
