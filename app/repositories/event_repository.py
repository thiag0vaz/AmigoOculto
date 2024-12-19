from app.models.event import Event
from app.models.user import User
from app import db
import random

class EventRepository:
    @staticmethod
    def save(event):
        db.session.add(event)
        db.session.commit()
        return event

    @staticmethod
    def get_event_by_id(event_id):
        return Event.query.get(event_id)

    @staticmethod
    def execute_draw(event_id):
        participants = User.query.filter_by(event_id=event_id).all()
        if len(participants) < 2:
            raise ValueError("O evento precisa de pelo menos 2 participantes para realizar o sorteio.")

        ids = [p.id for p in participants]
        random.shuffle(ids)

        for i, participant in enumerate(participants):
            participant.amigo_oculto_id = ids[(i + 1) % len(ids)]
        db.session.commit()

        return [{"user_id": p.id, "amigo_oculto_id": p.amigo_oculto_id} for p in participants]
