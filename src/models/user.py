from src.models.db import db 
import uuid


class User(db.Model):

    id = db.Column(db.String(36), primary_key=True, nullable=False)
    cognito_username = db.Column(db.String(36), primary_key=True, nullable=False)

    email = db.Column(db.String(120), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    nickname = db.Column(db.String(120), unique=False, nullable=False)

    teacher = db.Column(db.Boolean, nullable=False, default=False)
    # for s3 ids but this should be linked to a file 
    imageId = db.Column(db.String(20),nullable=True)
    
    modules = db.relationship('UserModule', back_populates='user')
    quizzes = db.relationship('UserQuizTake', back_populates='user')


    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'nickname': self.nickname,
            'teacher': self.teacher
        }
    

    def __init__(self):
        self.id = str(uuid.uuid4())
    def __repr__(self):
        return f"<User {self.username}>"
