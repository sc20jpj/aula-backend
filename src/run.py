from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS  # Import CORS
from src.models.db import db

from src.models.user import User
from src.models.module import Module
from src.models.quiz import Quiz
from src.models.lesson import Lesson

from src.models.user_module import UserModule
from src.models.user_quiz_take import UserQuizTake





from src import config

def configure_blueprints(app: object) -> None:
    from src.routes.user_route import users
    app.register_blueprint(users)


def create_app():
    app = Flask(__name__)
    
    with app.app_context():
        app.config.from_object(config)
        db.init_app(app=app)
        migrate = Migrate(app=app, db=db)

        db.create_all()
        configure_blueprints(app=app)

    # Enable CORS for all routes
    CORS(app)

    return app


    return app
