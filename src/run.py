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
from src.services import UserService
from flask_cognito import CognitoAuth



from src import config

def configure_blueprints(app):
    from src.routes.user_routes import users
    from src.routes.module_routes import modules
    from src.routes.user_modules_routes import user_modules
    from src.routes.lesson_routes import lessons
    from src.routes.document_routes import documents
    from src.errors.errors import error
  
    app.register_blueprint(users)
    app.register_blueprint(modules)
    app.register_blueprint(user_modules)
    app.register_blueprint(lessons)
    app.register_blueprint(documents)


    app.register_blueprint(error)



def lookup_cognito_user(payload):
    """Look up user in our database from Cognito JWT payload."""
    # for some reasons the admin auth sends the payload differently worth checking this later 
    try:
        return UserService.get_by_cognito_username(payload["cognito:username"])
    except KeyError:
        return UserService.get_by_cognito_username(payload["username"])


def create_app():
    app = Flask(__name__)
    
    with app.app_context():
        app.config.from_object(config)
        db.init_app(app=app)
        migrate = Migrate(app=app, db=db)
        cogauth = CognitoAuth(app=app)

        @cogauth.identity_handler
        def handle_identity(payload):
            return lookup_cognito_user(payload)
        CORS(app, resources={r"/*": {"origins": "*"}})
        with app.app_context():
                db.create_all()

        configure_blueprints(app=app)
 

    

    return app