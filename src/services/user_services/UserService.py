from src.models.db import db
from src.models.user import User

def add_user(data):

    new_user = User()

    for key, value in data.items():
        if hasattr(new_user, key):
            print(key)
            setattr(new_user, key, value)

    db.session.add(new_user)
    db.session.commit()


    return new_user

def get_user_by_id(user_id) -> User:

    queried_user = User.query.get(user_id)


    return queried_user




