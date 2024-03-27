from src.models.db import db 
from sqlalchemy.ext.associationproxy import association_proxy
import uuid


class Quiz(db.Model):
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    title = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    total_points = db.Column(db.Integer,nullable=False)


    module_id = db.Column(db.String(36), db.ForeignKey('module.id'), nullable=False)
    module = db.relationship('Module', back_populates='quizzes')
    users_takes = db.relationship('UserQuizTake', back_populates='quiz')


    # users who've taken the quiz
    # probably only use for admin 
    users = association_proxy('user_quiz_take', 'user')
    
    questions = db.relationship('Question', back_populates='quiz')

    """
    "id"
    "title"
    
    questions: [
        "title": 
        "number": 
        "choices": [
            {
                "title": "correct" 
                "correct": true

            }
        ]
    ]


    """



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