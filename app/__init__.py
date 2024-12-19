import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "sua-chave-secreta")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI", "sqlite:///amigo_oculto.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "sua-chave-jwt")
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.controllers.auth_controller import auth_blueprint
    from app.controllers.user_controller import user_blueprint
    from app.controllers.event_controller import event_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/api/auth")
    app.register_blueprint(user_blueprint, url_prefix="/api/users")
    app.register_blueprint(event_blueprint, url_prefix="/api/events")

    return app
