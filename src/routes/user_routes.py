from flask import Blueprint,request
from src.services import ResponseService
from sqlalchemy.exc import DataError
from http import HTTPStatus
from flask_cognito import cognito_auth_required,CognitoAuthError,current_cognito_jwt,current_user

from src.services import UserService,UserModuleService,ModuleService
users = Blueprint('users', __name__, url_prefix='/users')

# this route might not actually be needed
#  this is already done in run.py
@users.route('/check-auth', methods=['get'])
@cognito_auth_required
def check_auth():
    try:
        print(current_cognito_jwt)
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
    


# this probably be on the modules route
@users.route('/<moduleId>', methods=['get'])
@cognito_auth_required
def users_to_add(moduleId):
    try:
        data = {}

        current_user.modules 

        module = ModuleService.get_by_id(moduleId)
        users = UserService.get_all()
        users_on = module.users
        data["module"] = module.to_dict()


        users_not_on = [user for user in users if user not in users_on]
        
        users_on_data = []
        users_not_on_data = []

        print(module.users)
        # threading could be used here
        for user in users_on:
            if user.teacher == False:
                user_data = user.to_dict()
                users_on_data.append(user_data)
            else:
                data["teacher"] = user.name
        for user in users_not_on:
            if user.teacher == False:
                user_data = user.to_dict()
                users_not_on_data.append(user_data)

        data["users_on"] = users_on_data
        data["users_not_on"] = users_not_on_data
        print(data)
        return ResponseService.success(data=data)
    except DataError as e:
        return ResponseService.error(message="data error"), HTTPStatus.BAD_REQUEST   


 
