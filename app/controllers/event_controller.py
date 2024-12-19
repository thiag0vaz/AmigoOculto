from flask import Blueprint, jsonify, request
from app.repositories.event_repository import EventRepository
from app.schemas.event_schema import EventSchema
from app.exceptions.not_found_exception import NotFoundException
from app.utils.validation import validate_request_data

event_blueprint = Blueprint('event', __name__)

@event_blueprint.route('/', methods=['POST'])
def create_event():
    """Cria um novo evento."""
    data = request.json
    validated_data = validate_request_data(EventSchema(), data)
    event = EventRepository.create(validated_data)
    return jsonify(EventSchema().dump(event)), 201

@event_blueprint.route('/', methods=['GET'])
def get_all_events():
    """Retorna todos os eventos."""
    events = EventRepository.get_all()
    return jsonify(EventSchema(many=True).dump(events)), 200

@event_blueprint.route('/<int:event_id>', methods=['GET'])
def get_event(event_id):
    """Retorna detalhes de um evento específico."""
    event = EventRepository.get_event_by_id(event_id)
    if not event:
        raise NotFoundException("Evento")
    return jsonify(EventSchema().dump(event)), 200

@event_blueprint.route('/<int:event_id>/sorteio', methods=['POST'])
def execute_draw(event_id):
    try:
        resultado = EventRepository.execute_draw(event_id)
        return jsonify({"message": "Sorteio realizado com sucesso", "resultado": resultado}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400