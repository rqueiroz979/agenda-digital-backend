from flask import Blueprint, request, jsonify, current_app
from src.extensions import db
from src.models.user import User
import jwt
from datetime import datetime, timedelta

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    if not data.get('email') or not data.get('senha') or not data.get('nome'):
        return jsonify({'msg': 'nome, email e senha são obrigatórios'}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'msg': 'email já cadastrado'}), 400
    u = User(nome=data['nome'], email=data['email'])
    u.set_password(data['senha'])
    db.session.add(u)
    db.session.commit()
    return jsonify({'msg': '✅ Usuário criado com sucesso!'}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    if not data.get('email') or not data.get('senha'):
        return jsonify({'msg': 'email e senha obrigatórios'}), 400
    u = User.query.filter_by(email=data['email']).first()
    if not u or not u.check_password(data['senha']):
        return jsonify({'msg': 'credenciais inválidas'}), 401
    exp = datetime.utcnow() + timedelta(hours=current_app.config.get('JWT_EXP_HOURS', 8))
    token = jwt.encode({'user_id': u.id, 'exp': exp}, current_app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token, 'user': u.to_dict()})
