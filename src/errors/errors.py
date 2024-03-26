from flask import Blueprint
from http import HTTPStatus
from src.services import ResponseService

error = Blueprint('error', __name__)

@error.errorhandler(Exception)
def handle_error(error):
        return ResponseService.error(message="Exception"), HTTPStatus.NOT_FOUND


@error.app_errorhandler(404)
def not_found_error(e):
        return ResponseService.error(message="Resource not found"), HTTPStatus.NOT_FOUND
@error.app_errorhandler(400)
def not_found_error(e):
        print(error.__cause__)
        return ResponseService.error(message="Bad requqest"), HTTPStatus.BAD_REQUEST
@error.app_errorhandler(405)
def not_found_error(e):
        return ResponseService.error(message="Method not allowed"), HTTPStatus.METHOD_NOT_ALLOWED
@error.app_errorhandler(415)
def not_found_error(e):
        return ResponseService.error(message="media type"), HTTPStatus.UNSUPPORTED_MEDIA_TYPE
@error.app_errorhandler(500)
def internal_server_error(e):
        return ResponseService.error(message="Internal server error"), HTTPStatus.INTERNAL_SERVER_ERROR
@error.app_errorhandler(401)
def internal_server_error(e):
        return ResponseService.error(message="Unauthorised"), HTTPStatus.UNAUTHORIZED
