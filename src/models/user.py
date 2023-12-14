from src.models.db import db
import uuid

class User(db.Model):
    id = db.Column(db.String(16), primary_key=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self):
        self.id = str(uuid.uuid4())
    def __repr__(self):
        return f"<User {self.username}>"