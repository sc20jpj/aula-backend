from flask import Blueprint,request
from src.services import ResponseService
from sqlalchemy.exc import DataError
from http import HTTPStatus
from flask_cognito import cognito_auth_required

from src.services import UserModuleService,UserService
user_modules = Blueprint('user-modules', __name__, url_prefix='/user-modules')


@user_modules.route('/<module_id>', methods=['post'])
@cognito_auth_required
def add_users_to_module(module_id):
    try:
        data = request.json 
        user_modules = UserModuleService.add_users(users=data["users"],module_id=module_id)

         
        data = {
            "users": []
        }
        for user_module in user_modules:
            data["users"].append(user_module.user.to_dict())

    
        return ResponseService.success(data=data)
    except DataError as e:
        return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST

    except Exception as e:
        return ResponseService.error(message=e), HTTPStatus.INTERNAL_SERVER_ERROR
    


