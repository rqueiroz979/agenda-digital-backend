from src import create_app

# Ponto de entrada principal
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
