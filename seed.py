
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from main import create_app
from extensions import db
from src.models.user import User

def seed_db():
    app = create_app()
    with app.app_context():
        print("Verificando e adicionando usuário admin...")
        if not User.query.filter_by(email="admin@empresa.com").first():
            admin_user = User(nome="Admin", email="admin@empresa.com")
            admin_user.set_password("123456")
            db.session.add(admin_user)
            db.session.commit()
            print("✅ Usuário admin 'admin@empresa.com' criado com sucesso!")
        else:
            print("Usuário admin 'admin@empresa.com' já existe.")

if __name__ == "__main__":
    seed_db()


