from src.models.db import db 
import uuid


class UserModule(db.Model):
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'),primary_key=True)
    module_id = db.Column(db.String(36), db.ForeignKey('module.id'),primary_key=True)
    points = db.Column(db.Integer,nullable=True)
    
    user = db.relationship('User', back_populates='user_modules')
    module = db.relationship('Module', back_populates='user_modules')


    
    def to_dict(self):
        return {
            'points': self.points,
        }

