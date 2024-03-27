from src.models.db import db 
import uuid


class Question(db.Model):
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    
    description = db.Column(db.Text(), unique=False, nullable=False)

    choices = db.relationship('Choice', back_populates='question')

    #  the points a questions is worth
    points = db.Column(db.Text(), unique=False, nullable=False)

    quiz = db.relationship('Quiz', back_populates='questions')

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'points': self.description,
        }

    def __init__(self):
        self.id = str(uuid.uuid4())
    def __repr__(self):
        return f"<Quiz {self.title}>"