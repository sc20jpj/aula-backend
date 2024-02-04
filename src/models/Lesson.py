from src.models.db import db 
import uuid


class Lesson(db.Model):

    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    
    
    module_id = db.Column(db.String(16), db.ForeignKey('module.id'), nullable=False)
    module = db.relationship('Module', back_populates='lessons')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'description': self.code,
        }

    def __init__(self):
        self.id = str(uuid.uuid4())
    def __repr__(self):
        return f"<Lesson {self.name}>"
