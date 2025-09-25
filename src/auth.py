import jwt
from flask import request, jsonify, current_app
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        auth = request.headers.get('Authorization', None)
        if auth and auth.startswith('Bearer '):
            token = auth.split(' ')[1]
        if not token:
            return jsonify({'msg': 'Token is missing!'}), 401
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            request.user_payload = payload
        except jwt.ExpiredSignatureError:
            return jsonify({'msg': 'Token expired'}), 401
        except Exception:
            return jsonify({'msg': 'Token invalid'}), 401
        return f(*args, **kwargs)
    return decorator
