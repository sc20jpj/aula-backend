from flask import Blueprint,request
from src.services import ResponseService
from sqlalchemy.exc import DataError
from http import HTTPStatus
from flask_cognito import cognito_auth_required,CognitoAuthError,current_cognito_jwt,current_user

from src.services import UserService,UserModuleService,ModuleService
users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/check-auth', methods=['get'])
@cognito_auth_required
def check_auth():
    try:
        
        new_user = UserService.get_by_cognito_username(current_cognito_jwt['cognito:username'])
        return ResponseService.success(data=new_user.to_dict())
    except DataError as e:
        return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST

    except Exception as e:
        return ResponseService.error(message=e), HTTPStatus.NOT_FOUND
    

@users.route('/new-user', methods=['post'])
@cognito_auth_required
def add_user():
    try:
        data = request.json
        new_user = UserService.add(data=data)
        return ResponseService.success(data=new_user.to_dict())
    except DataError as e:
        return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST

    except Exception as e:
        return ResponseService.error(message=e), HTTPStatus.NOT_FOUND
    

    
@users.route('/all', methods=['get'])
@cognito_auth_required
def all_users():
    try:
        data = {}

        
        users = UserService.get_all()
        users_array = []
        for user in users:
            if user.teacher == False:
                users_array.append(user.to_dict())

        data = users_array

        return ResponseService.success(data=data)
    except DataError as e:
        return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST

    except Exception as e:
        return ResponseService.error(message=e), HTTPStatus.NOT_FOUND


    


@users.route('/<moduleId>', methods=['get'])
@cognito_auth_required
def all_users_on_module(moduleId):
    try:
        data = {}

        current_user.modules 
        module = ModuleService.get_by_id(moduleId)
        users = module.users
        users_array = []

        for user in users:
            if user.teacher == False:
                user_data = user.to_dict()
                users_array.append(user_data)
        
        data["users"] = users_array

        return ResponseService.success(data=data)
    except DataError as e:
        return ResponseService.error(message="data error"), HTTPStatus.BAD_REQUEST   
