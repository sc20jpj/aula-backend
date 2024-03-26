from src.models.db import db 
import uuid


class UserQuizTake(db.Model):
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'),primary_key=True)
    quiz_id = db.Column(db.String(36), db.ForeignKey('quiz.id'),primary_key=True)
    points = db.Column(db.Integer,nullable=False)
    
    user = db.relationship('User', back_populates='quizzes')
    quiz = db.relationship('Quiz', back_populates='users')


    def to_dict(self):
        return {
            'points': self.points,
        }

    def __init__(self):
        self.id = str(uuid.uuid4())