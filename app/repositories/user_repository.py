from app.models.user import User
from app import db

class UserRepository:
    @staticmethod
    def create(data):
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_users_by_event(event_id):
        return User.query.filter_by(event_id=event_id).all()

    @staticmethod
    def assign_event_to_user(user_id, event_id):
        user = User.query.get(user_id)
        if not user:
            return None
        user.event_id = event_id
        db.session.commit()
        return user
