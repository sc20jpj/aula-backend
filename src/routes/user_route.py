from flask import Blueprint
from src.services import ResponseService
from http import HTTPStatus

classes = Blueprint('classes', __name__, url_prefix='/classes')


@classes.route('', methods=['get', 'post'])
def get_all_classes():
    try:
        data = {
            "message": "hello"
        }
        return ResponseService.success(data=data)
    
    except Exception as e:
        return ResponseService.error(message=e), HTTPStatus.NOT_FOUND

