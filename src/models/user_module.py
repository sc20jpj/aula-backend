from src.models.db import db 
import uuid


class UserModule(db.Model):
    user_id = db.Column(db.String(16), db.ForeignKey('user.id'),primary_key=True)
    module_id = db.Column(db.String(16), db.ForeignKey('module.id'),primary_key=True)
    points = db.Column(db.Integer,nullable=False)
    
    user = db.relationship('User', back_populates='modules')
    module = db.relationship('Module', back_populates='users')

    
    def to_dict(self):
        return {
            'points': self.points,
        }

    def __init__(self):
        self.id = str(uuid.uuid4())


