from src.models.db import db 
import uuid


class Class(db.Model):

    id = db.Column(db.String(16), primary_key=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    code = db.Column(db.String(120), unique=True, nullable=False)
    
    users = db.relationship('UserClass', back_populates='assigned_class')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
        }

    def __init__(self):
        self.id = str(uuid.uuid4())
    def __repr__(self):
        return f"<User {self.username}>"
