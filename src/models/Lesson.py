from src.models.db import db 
import uuid


class Lesson(db.Model):

    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)

    module_id = db.Column(db.String(36), db.ForeignKey('module.id'), nullable=False)
    module = db.relationship('Module', back_populates='lessons')
    documents = db.relationship('Document', back_populates='lesson')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }

    def __init__(self,module_id):
        self.id = str(uuid.uuid4())
        self.module_id = module_id
    def __repr__(self):
        return f"<Lesson {self.name}>"
