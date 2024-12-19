from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=True)
    amigo_oculto_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    amigo_oculto = db.relationship('User', remote_side=[id])

    def __init__(self, username, email, password, event_id=None):
        """
        Inicializa um novo usuário, gerando o hash da senha.
        """
        self.username = username
        self.email = email
        self.set_password(password)
        self.event_id = event_id

    def set_password(self, password):
        """
        Gera o hash da senha e a armazena no campo `password`.
        """
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        """
        Verifica se a senha fornecida corresponde ao hash armazenado.

        Args:
            password (str): A senha em texto plano.

        Returns:
            bool: True se a senha for válida, False caso contrário.
        """
        return check_password_hash(self.password, password)

    def __repr__(self):
        """
        Representação legível do objeto User.
        """
        return f"<User {self.username}>"
