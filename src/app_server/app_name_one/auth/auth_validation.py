from marshmallow import Schema, fields, validate

class UserBodySchema(Schema):
    email = fields.Str(
        required=True,
        validate=[
            validate.Length(min=1, error='Email is required'),
            validate.Email(error='Email is invalid')
        ]
    )
    password = fields.Str(
        required=True,
        validate=validate.Length(min=4, error='Password must be at least 4 characters long')
    )

class CreateUser(Schema):
    body = fields.Nested(UserBodySchema)
    query = fields.Dict(keys=fields.Str(),values=fields.Raw(), required=False,missing={})
    params = fields.Dict(keys=fields.Str(),values=fields.Raw(), required=False,missing={})
    cookies = fields.Dict(keys=fields.Str(),values=fields.Raw(), required=False,missing={})


