class AppException(Exception):
    """
    Classe base para todas as exceções personalizadas da aplicação.
    """
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        """
        Converte a exceção para um dicionário para serialização em JSON.
        """
        return {"error": self.message}
