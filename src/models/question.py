from src.models.db import db 
import uuid


class Question(db.Model):
    id = db.Column(db.String(16), primary_key=True, nullable=False)
    
    #arugement to be made about naming of this variable

    question = db.Column(db.Text(), unique=False, nullable=False)
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
        }

    def __init__(self):
        self.id = str(uuid.uuid4())
    def __repr__(self):
        return f"<Quiz {self.title}>"