from src.models.db import db 
import uuid


class Choice(db.Model):
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    
    description = db.Column(db.Text(), unique=False, nullable=False)
    
    # correct is set by teacher when creating a quiz
    correct = db.Column(db.Text(), unique=False, nullable=False)
    question = db.relationship('Question', back_populates='choices')

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.description,
            'correct': self.correct,
        }

    def __init__(self):
        self.id = str(uuid.uuid4())
    def __repr__(self):
        return f"<Quiz {self.title}>"