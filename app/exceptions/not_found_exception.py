from .base_exception import AppException

class NotFoundException(AppException):
    """
    Exceção para recursos não encontrados.
    """
    def __init__(self, resource_name="Recurso"):
        super().__init__(f"{resource_name} não encontrado", status_code=404)
