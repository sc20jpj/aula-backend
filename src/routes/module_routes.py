from flask import Blueprint,request
from src.models.user import User
from src.services import ResponseService
from sqlalchemy.exc import DataError,IntegrityError
from http import HTTPStatus
from flask_cognito import cognito_auth_required,cognito_group_permissions,CognitoAuthError,current_user

from src.services import ModuleService,UserModuleService
modules = Blueprint('modules', __name__, url_prefix='/modules')

@modules.route('/all', methods=['get'])
@cognito_auth_required
@cognito_group_permissions(['teachers'])
def all_modules():
    try:
        data = {}

        modules = ModuleService.get_all()
        modules_array = []
        for module in modules:
            modules_array.append(module.to_dict())
        data["modules"] = modules_array

        return ResponseService.success(data=data)
    except DataError as e:
        return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST

    except Exception as e:
        return ResponseService.error(message=e), HTTPStatus.NOT_FOUND


@modules.route('', methods=['get'])
@cognito_auth_required
def all_modules_user():
    try:
        data = {}



        modules = ModuleService.get_all()
        modules_array = []
        for module in modules:
            module_data = module.to_dict()

            for user in module.users:
                if user.teacher == 1:
                    module_data["teacher"] = user.name
            modules_array.append(module_data)

        print(modules_array)
        data["modules"] = modules_array

        return ResponseService.success(data=data)
    except IntegrityError as e:
        return ResponseService.error(message="Module already exists"), HTTPStatus.CONFLICT
    except DataError as e:
        return ResponseService.error(message="data error"), HTTPStatus.BAD_REQUEST
    
@modules.route('', methods=['post'])
@cognito_auth_required
@cognito_group_permissions(['teachers'])
def add_module():
    try:
        data = request.json
    
        new_module = ModuleService.add(data=data)

        new_user_module = UserModuleService.add(user_id=current_user.id,module_id=new_module.id)
        return ResponseService.success(data=new_user_module.to_dict())
    
    except DataError as e:
        return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        return ResponseService.error(message="Module already exists"), HTTPStatus.CONFLICT
    except Exception as e:
        return ResponseService.error(message="Exception"), HTTPStatus.INTERNAL_SERVER_ERROR
    

@modules.route('/<moduleId>', methods=['delete'])
@cognito_auth_required
@cognito_group_permissions(['teachers'])
def delete_module(moduleId):
    try:
        new_module = ModuleService.delete(module_id=moduleId)
        return ResponseService.success(data=new_module.to_dict())
    except DataError as e:
        return ResponseService.error(message="data"), HTTPStatus.BAD_REQUEST

    except Exception as e:
        return ResponseService.error(message=e), HTTPStatus.NOT_FOUND