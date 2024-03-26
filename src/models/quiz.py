from src.models.db import db 
import uuid


class Quiz(db.Model):
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    title = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    total_points = db.Column(db.Integer,nullable=False)


    module_id = db.Column(db.String(36), db.ForeignKey('module.id'), nullable=False)
    module = db.relationship('Module', back_populates='quizzes')
    users = db.relationship('UserQuizTake', back_populates='quiz')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
        }

    def __init__(self):
        self.id = str(uuid.uuid4())
    def __repr__(self):
        return f"<Quiz {self.title}>"