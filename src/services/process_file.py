import base64
from datetime import timedelta,datetime
from src.services import FileService,DocumentService
def process_file(file_data, lesson_id):
        filename = file_data["name"]
        base64String = file_data["base64"]
        file_content = base64.b64decode(base64String)

        current_datetime = datetime.utcnow()
        tomorrow_datetime = current_datetime + timedelta(days=1)
        print("Tomorrow's date:", tomorrow_datetime)

        file_object = FileService.add(name=filename, data=file_content)
        presigned_url = FileService.get_url(file_object.key)

        data = {
            "name": filename,
            "s3_url": presigned_url,
            "s3_url_expiry": tomorrow_datetime
        }
        DocumentService.add(data, lesson_id=lesson_id)