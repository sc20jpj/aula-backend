from flask import Blueprint,request
from src.services import ResponseService
from sqlalchemy.exc import DataError
from http import HTTPStatus
from flask_cognito import cognito_auth_required,CognitoAuthError

from src.services.user_services import UserService
users = Blueprint('users', __name__, url_prefix='/users')

@users.route('', methods=['get'])
@cognito_auth_required
def get_all_classes():
    try: 
        # data = {
        #     "message": "hello"
        # }
        return ResponseService.success(data="hello")
    except CognitoAuthError as exception:
        return ResponseService.error(message=exception), HTTPStatus.UNAUTHORIZED
    except Exception as e:
        return ResponseService.error(message=e), HTTPStatus.NOT_FOUND
    

# This route is only for development will be switched by a lambda trigger when deployed 
@users.route('/new-user', methods=['post'])
def add_user():
    try:
        data = request.json
        print(data)
        new_user = UserService.add_user(data=data)
        return ResponseService.success(data=new_user.to_dict())
    # except DataError as e:
    #     return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST

    except Exception as e:
        return ResponseService.error(message=e), HTTPStatus.NOT_FOUND

