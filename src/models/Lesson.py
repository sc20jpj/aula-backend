from src.models.db import db 
import uuid


class Lesson(db.Model):

    id = db.Column(db.String(16), primary_key=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    assigned_class = db.relationship('Class', back_populates='quizzes')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
        }

    def __init__(self):
        self.id = str(uuid.uuid4())
    def __repr__(self):
        return f"<Class {self.name}>"
