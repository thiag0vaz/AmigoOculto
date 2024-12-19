from .base_exception import AppException

class ValidationException(AppException):
    """
    Exceção para erros de validação.
    """
    def __init__(self, errors, message="Erro de validação"):
        super().__init__(message, status_code=400)
        self.errors = errors

    def to_dict(self):
        """
        Inclui os erros de validação no dicionário de resposta.
        """
        response = super().to_dict()
        response["details"] = self.errors
        return response
