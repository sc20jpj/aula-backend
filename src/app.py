from src.run import create_app
from src.services import ResponseService
from http import HTTPStatus

app = create_app()

@app.errorhandler(404)
def not_found_error(error):
        return ResponseService.error(message="Resource not found"), HTTPStatus.NOT_FOUND
@app.errorhandler(500)
def internal_server_error(error):
        return ResponseService.error(message="Internal server error"), HTTPStatus.INTERNAL_SERVER_ERROR

if __name__ == "__main__":
    app.run(debug=True)
