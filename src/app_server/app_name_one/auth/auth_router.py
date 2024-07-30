from flask import Blueprint, jsonify, request
from . import auth_controller
from src.app_server.decorators import validator
from . import auth_validation
from src.app_server.utils.resSender import send_res

auth_bp = Blueprint('auth_bp',__name__)

@auth_bp.post("/register")
@validator.validat_schema(auth_validation.CreateUser())
def create_user():
    print(request.validated_data)
    # result = auth_controller.create_user()
    result = request.validated_data
    return send_res(
        status=201,
        data= result,
        message='User created successfully',
    )