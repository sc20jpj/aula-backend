from src.models.db import db 
import uuid


class UserQuestionChoice(db.Model):

    '''
    This table represents the individual choice a user selects for a question
    You could make this is specifically multichoice
    Could make for longer answers
    '''
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'),primary_key=True)
    question_id = db.Column(db.String(36), db.ForeignKey('question.id'),primary_key=True)
    choice_id = db.Column(db.String(36), db.ForeignKey('choice.id'),primary_key=True)

    
    user = db.relationship('User', back_populates='quizzes')
    quiz = db.relationship('Quiz', back_populates='users')


# current_user.modules 

    def to_dict(self):
        return {
            'points': self.points,
        }

    def __init__(self):
        self.id = str(uuid.uuid4())

# module.