from flask_jwt_extended import get_jwt_identity
from app.repositories.user_repository import UserRepository
from app.exceptions.authorization_exception import UnauthorizedException

def get_authenticated_user():
    """
    Recupera o usuário autenticado com base no token JWT.

    Returns:
        User: O objeto do usuário autenticado.

    Raises:
        UnauthorizedException: Se o usuário não for encontrado ou não estiver autenticado.
    """
    user_id = get_jwt_identity()
    user = UserRepository.get_user_by_id(user_id)
    if not user:
        raise UnauthorizedException("Usuário não autenticado")
    return user
