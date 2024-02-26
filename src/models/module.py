from src.models.db import db 
from sqlalchemy.ext.associationproxy import association_proxy
import uuid


class Module(db.Model):

    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    code = db.Column(db.String(120), unique=True, nullable=False)
    
    user_modules = db.relationship('UserModule', back_populates='module')
    users = association_proxy('user_modules', 'user')

    quizzes = db.relationship('Quiz', back_populates='module')
    lessons = db.relationship('Lesson', back_populates='module')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
        }

    def __init__(self):
        self.id = str(uuid.uuid4())
    def __repr__(self):
        return f"<Module {self.name}>"
