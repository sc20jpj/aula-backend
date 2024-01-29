from flask import Flask
from flask_migrate import Migrate
from models.classrooms.db import db
from models.classrooms.user import User
from src import config 


def configure_blueprints(app: object) -> None:
    from src.routes.user_route import classes    
    app.register_blueprint(classes)


def create_app():
    app = Flask(__name__)
    
    with app.app_context():
        app.config.from_object(config)
        db.init_app(app=app)
        migrate = Migrate(app=app,db=db)

        db.create_all()
        configure_blueprints(app=app)

    return app