from src.models.db import db
from src.models.user import User

def add(data):

    new_user = User()

    for key, value in data.items():
        if hasattr(new_user, key):
            print(key)
            setattr(new_user, key, value)

    db.session.add(new_user)
    db.session.commit()


    return new_user

def get_by_cognito_username(cognito_username) -> User:

    queried_user = User.query.filter_by(cognito_username=cognito_username).one_or_none()


    return queried_user

def get_by_id(user_id) -> User:

    queried_user = User.query.get(user_id)


    return queried_user

def get_all(user_id) -> [User]:

    users = User.query.all()


    return users




