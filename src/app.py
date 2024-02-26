from flask import url_for
from src.run import create_app
from src.services import ResponseService
from http import HTTPStatus
import urllib
app = create_app()



if __name__ == "__main__":

        app.run(debug=True)
