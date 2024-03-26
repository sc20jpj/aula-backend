import base64
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from flask import Blueprint,request,current_app
from src.models.user import User
from src.services import ResponseService
from sqlalchemy.exc import DataError,IntegrityError
from http import HTTPStatus
from flask_cognito import cognito_auth_required,cognito_group_permissions,CognitoAuthError,current_user

from src.services import LessonService,FileService,DocumentService,ModuleService
lessons = Blueprint('lessons', __name__, url_prefix='/lessons')


def process_file(file,lesson_id):
    print ("current_app is " ,current_app)

    filename = file["name"]
    file_type = file["file_type"]
    print(filename)
    base64String = file["base64"]
    file  =  base64.b64decode(base64String)

    current_datetime = datetime.utcnow()
    tomorrow_datetime = current_datetime + timedelta(days=1)
    print("tommorows dates",tomorrow_datetime)
    object = FileService.add(name=filename,data=file)
    presigned_url = FileService.get_url(object.key)

    print(presigned_url)
    
    data = {
        "name": filename,
        "s3_url": presigned_url,
        "file_type":  file_type,
        "s3_url_expiry": tomorrow_datetime
    }
    return DocumentService.add(data,lesson_id=lesson_id)

# this route could be moved to lessons
@lessons.route('/<lessson_id>', methods=['get'])
@cognito_auth_required
@cognito_group_permissions(['teachers'])
def get_full_lessson(lessson_id):

    try:
        lessson = LessonService.get_by_id(id=lessson_id)
        lessson_dic = lessson.to_dict()
        current_datetime = datetime.utcnow()
        tomorrow_datetime = current_datetime + timedelta(days=1)
        documents = []
        for document in lessson.documents:
            if current_datetime >= document.s3_url_expiry:
                presigned_url = FileService.get_url(document.name)
                DocumentService.set_s3_url(document,presigned_url)

            documents.append(document.to_dict())

        lessson_dic["documents"] = documents 

        return ResponseService.success(data=lessson_dic)
    
    except DataError as e:
        return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        return ResponseService.error(message="Lesson already exists"), HTTPStatus.CONFLICT
    except Exception as e:
        return ResponseService.error(message="Exception"), HTTPStatus.INTERNAL_SERVER_ERROR



@lessons.route('/<module_id>', methods=['post'])
@cognito_auth_required
@cognito_group_permissions(['teachers'])
def add_lesson(module_id):
    try:
        data = request.json

        new_lesson = LessonService.add(data=data,module_id=module_id)
     
        files = data["files"]

        # the max workers need to be changed
        # not sure whats a good amount


        # with ThreadPoolExecutor(max_workers=len(files)) as executor:
        for file in files:
                # executor.submit(process_file, file=file, lesson_id=new_lesson.id)
            process_file(file=file,lesson_id=new_lesson.id)

        return ResponseService.success(data=new_lesson.to_dict())
    
    except DataError as e:
        return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        return ResponseService.error(message="Lesson already exists"), HTTPStatus.CONFLICT
    # except Exception as e:
    #     return ResponseService.error(message="Exception"), HTTPStatus.INTERNAL_SERVER_ERROR

@lessons.route('/edit/<lessson_id>', methods=['post'])
@cognito_auth_required
@cognito_group_permissions(['teachers'])
def edit_lessson(lessson_id):

    try:
        lessson = LessonService.get_by_id(id=lessson_id)
        
        data = request.json

        files = data["files"]

        print("reached")
        # this multithreadign doesnt work
        # not thread safe
        # with ThreadPoolExecutor(max_workers=len(files)) as executor:
    
        for file in files:
                # executor.submit(process_file, file=file, lesson_id=lessson.id)
                
            process_file(file=file,lesson_id=lessson.id)
        return ResponseService.success(data=lessson.to_dict())

    except DataError as e:
        return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        return ResponseService.error(message="Lesson already exists"), HTTPStatus.CONFLICT
    # except Exception as e:
    #     return ResponseService.error(message="Exception"), HTTPStatus.INTERNAL_SERVER_ERROR


# this route could be moved to module

@lessons.route('/all/<module_id>', methods=['get'])
@cognito_auth_required
def get_all_lessons_for_module(module_id):

    try:
        module = ModuleService.get_by_id(module_id=module_id)
        module_dic = module.to_dict()
        lessons = []
        for lesson in module.lessons:
            files = []
            lesson_dict = lesson.to_dict()
            
            for document in lesson.documents:
                current_datetime = datetime.now()

                if document.s3_url_expiry <= current_datetime:
                    tomorrow_datetime = current_datetime + timedelta(days=1)
                    print("tommorows dates",tomorrow_datetime)
                    presigned_url = FileService.get_url(document.name)
                    up_to_date_document = DocumentService.set_s3_url(document,presigned_url)
                    files.append(up_to_date_document.to_dict())

                else:
                    files.append(document.to_dict())

            lesson_dict["files"] = files
            lessons.append(lesson_dict)
        
        module_dic["lessons"]= lessons
        print(module_dic["lessons"])
        return ResponseService.success(data=module_dic)
    
    except DataError as e:
        return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        return ResponseService.error(message="Lesson already exists"), HTTPStatus.CONFLICT
    except Exception as e:
        print(e)
        return ResponseService.error(message={e.__cause__}), HTTPStatus.INTERNAL_SERVER_ERROR
    
