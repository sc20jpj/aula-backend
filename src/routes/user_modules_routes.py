from flask import Blueprint,request
from src.services import ResponseService
from sqlalchemy.exc import DataError
from http import HTTPStatus
from flask_cognito import cognito_auth_required,cognito_group_permissions,CognitoAuthError,current_user

from src.services import UserModuleService
user_modules = Blueprint('modules', __name__, url_prefix='/user-modules')


@user_modules.route('/:moduleId', methods=['post'])
@cognito_auth_required
def add_user_to_module(moduleId):
    try:
        new_user = UserModuleService.add(userId=current_user.id,classId=moduleId)
        return ResponseService.success(data=new_user.to_dict())
    except DataError as e:
        return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST

    except Exception as e:
        return ResponseService.error(message=e), HTTPStatus.NOT_FOUND
    

