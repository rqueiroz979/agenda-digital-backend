from src import create_app
from src.extensions import db, migrate

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
