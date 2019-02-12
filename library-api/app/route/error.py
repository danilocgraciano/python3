from flask import Blueprint, request
from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

error = Blueprint("error", __name__)

@error.app_errorhandler(ValidationError)
def validation_error(e):
    response = jsonify({'error': 'bad request', 'message': e.args[0]})
    response.status_code = 400
    return response

@error.app_errorhandler(IntegrityError)
def validation_error(e):
    response = jsonify({'error': 'bad request', 'message': e.args[0]})
    response.status_code = 400
    return response

@error.app_errorhandler(Exception)
def validation_error(e):
    response = jsonify({'error': 'internal server error', 'message': e.args[0]})
    response.status_code = 500
    return response