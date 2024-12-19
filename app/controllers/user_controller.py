from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.routes import get_authenticated_user
from app.repositories.user_repository import UserRepository
from app.repositories.event_repository import EventRepository
from app.schemas.user_schema import UserSchema
from app.exceptions.not_found_exception import NotFoundException
from app.exceptions.authorization_exception import UnauthorizedException
from app.utils.validation import validate_request_data

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """Retorna informações do usuário autenticado."""
    user = get_authenticated_user()
    if not user:
        raise NotFoundException("Usuário")
    return jsonify(UserSchema().dump(user)), 200

@user_blueprint.route('/', methods=['POST'])
def create_user():
    """Cria um novo usuário."""
    data = request.json
    validated_data = validate_request_data(UserSchema(), data)
    user = UserRepository.create(validated_data)
    return jsonify(UserSchema().dump(user)), 201

@user_blueprint.route('/event/<int:event_id>', methods=['GET'])
@jwt_required()
def get_users_by_event(event_id):
    """Lista todos os usuários de um evento específico."""
    current_user = get_authenticated_user()
    if current_user.event_id != event_id:
        raise UnauthorizedException("Você não tem permissão para acessar este evento")

    users = UserRepository.get_users_by_event(event_id)
    if not users:
        raise NotFoundException("Usuários para o evento")
    return jsonify(UserSchema(many=True).dump(users)), 200

@user_blueprint.route('/<int:user_id>/event/<int:event_id>', methods=['PUT'])
@jwt_required()
def assign_user_to_event(user_id, event_id):
    user = UserRepository.get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    event = EventRepository.get_event_by_id(event_id)
    if not event:
        return jsonify({"error": "Evento não encontrado"}), 404

    UserRepository.assign_event_to_user(user_id, event_id)
    return jsonify({"message": "Usuário associado ao evento com sucesso"}), 200