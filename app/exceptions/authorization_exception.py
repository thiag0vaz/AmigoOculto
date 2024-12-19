from .base_exception import AppException

class UnauthorizedException(AppException):
    """
    Exceção para acessos não autorizados.
    """
    def __init__(self, message="Acesso não autorizado"):
        super().__init__(message, status_code=403)
