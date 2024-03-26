import base64
from datetime import datetime,timedelta
from flask import Blueprint,request
from src.services import ResponseService
from sqlalchemy.exc import DataError,IntegrityError
from http import HTTPStatus
from flask_cognito import cognito_auth_required,cognito_group_permissions,CognitoAuthError,current_user

from src.services import LessonService,FileService,DocumentService
documents = Blueprint('documents', __name__, url_prefix='/documents')


