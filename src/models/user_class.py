from src.models.db import db 
import uuid


class UserClass(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'),primary_key=True)
    points = db.Column(db.Integer,nullable=False)
    
    user = db.relationship('User', back_populates='classes')
    assigned_class = db.relationship('Class', back_populates='users')

    
    def to_dict(self):
        return {
            'points': self.points,
        }

    def __init__(self):
        self.id = str(uuid.uuid4())


