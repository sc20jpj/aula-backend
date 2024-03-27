from datetime import datetime,timedelta
from src.models.db import db
from src.models.document import Document

def add(data,lesson_id):

    new_document = Document(lesson_id=lesson_id)
    print("doc service is running")
    for key, value in data.items():
        if hasattr(new_document, key):
            print(key)
            setattr(new_document, key, value)

    try:
        print("Committing transaction")
        print("reached to transaction")
        db.session.add(new_document)
        db.session.commit()
    except Exception as e:
        print(f"Error committing transaction: {e}")
        db.session.rollback()
        raise e


    return new_document
def set_s3_url(document,s3_url):
    current_datetime = datetime.utcnow()
    tomorrow_datetime = current_datetime + timedelta(days=1)

    document.s3_url_expiry = tomorrow_datetime
    document.s3_url = s3_url
    db.session.commit()
    return document
