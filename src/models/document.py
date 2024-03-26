import uuid
import datetime
from src.models.db import db 
from sqlalchemy.ext.associationproxy import association_proxy



class Document(db.Model):

    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    file_type = db.Column(db.String(120), nullable=False)
    s3_url = db.Column(db.Text, nullable=False)
    s3_url_expiry = db.Column(db.DateTime, nullable=False)


    lesson_id = db.Column(db.String(36), db.ForeignKey('lesson.id'), nullable=False)
    lesson = db.relationship('Lesson', back_populates='documents')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            "file_type": self.file_type,
            's3_url': self.s3_url
        }

    def __init__(self,lesson_id):
        self.id = str(uuid.uuid4())
        self.lesson_id = lesson_id
    def __repr__(self):
        return f"<Module {self.name}>"