from src import create_app
from src.extensions import db
from src.models.user import User

app = create_app()
app.app_context().push()

def create_admin():
    if User.query.filter_by(email='admin@empresa.com').first():
        print('admin já existe')
        return
    u = User(nome='Admin', email='admin@empresa.com', is_admin=True)
    u.set_password('123456')
    db.session.add(u)
    db.session.commit()
    print('✅ Usuário admin criado: admin@empresa.com / 123456')

if __name__ == '__main__':
    create_admin()
