from functools import wraps
from marshmallow import ValidationError
from flask import request, jsonify

def validat_schema(marshlw_schema):
    """
    Decorator to validate request data using a Marshmallow schema.
    """
    def decorator(func):
        @wraps(func)
        def decorated_wrapper(*args,**kwargs):
            # extract data from request
            data = {
                'body': request.get_json() or {},
                'query': request.args.to_dict() ,
                'params': request.view_args,
                'cookies': request.cookies,
            }

            # validate json data
            try:
                validated_data = marshlw_schema.load(data)
            except ValidationError as err:
                return jsonify({'success':False,'message':err.messages}), 400

            # Add validated data to the request context
            request.validated_data = validated_data

            return func(*args, **kwargs)
        return decorated_wrapper
    return decorator