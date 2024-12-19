from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from app.repositories.user_repository import UserRepository

class AuthService:
    @staticmethod
    def authenticate(email, password):
        user = UserRepository.get_user_by_email(email)
        if user and check_password_hash(user.password, password):
            tokens = {
                "access_token": create_access_token(identity=user.id),
                "refresh_token": create_refresh_token(identity=user.id)
            }
            return tokens, user
        return None, None
