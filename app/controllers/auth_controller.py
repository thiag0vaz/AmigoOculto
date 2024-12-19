from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app.exceptions.validation_exception import ValidationException
from app.exceptions.authorization_exception import UnauthorizedException
from app.repositories.user_repository import UserRepository
from werkzeug.security import check_password_hash

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    """Realiza login e retorna tokens JWT."""
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        raise ValidationException(errors={"email": "Email é obrigatório", "password": "Senha é obrigatória"})

    user = UserRepository.get_user_by_email(email)
    if not user or not check_password_hash(user.password, password):
        raise UnauthorizedException("Credenciais inválidas")

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200

@auth_blueprint.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """Gera um novo access token usando refresh token."""
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify({"access_token": new_access_token}), 200
