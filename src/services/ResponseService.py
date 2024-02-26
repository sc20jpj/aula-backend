import json
from flask import jsonify
from http import HTTPStatus    

def success(data,links=None):
    response = {
        "status": "Ok"
    }
    if data != None:
        response["data"] = data
    if links != None:
        response["links"] = links
    return jsonify(response)

def error(message):
    response = {
        "error": "error",
    }
    if message is not None:
        response["message"] = message

    return jsonify(response)

