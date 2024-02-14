from flask import Blueprint,request
from src.services import ResponseService
from sqlalchemy.exc import DataError
from http import HTTPStatus
from flask_cognito import cognito_auth_required,CognitoAuthError,current_cognito_jwt,current_user

from src.services import UserService,UserModuleService
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
        print(data)
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

        
        print(current_user)
        users = UserService.get_all()
        users_array = []
        for user in users:
            users_array.append(user.to_dict())
        data["users"] = users_array

        return ResponseService.success(data=data)
    except DataError as e:
        return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST

    except Exception as e:
        return ResponseService.error(message=e), HTTPStatus.NOT_FOUND
    


    
