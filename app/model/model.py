# import required libraries and modules
from marshmallow import Schema, fields, validate

# define list of valid vields
VALID_CMD = ('filter', 'map', 'sort', 'limit', 'unique')


# creating schema according to required form
class RequestSchema(Schema):
    cmd1 = fields.Str(required=True, validate=validate.OneOf(VALID_CMD))
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True, validate=validate.OneOf(VALID_CMD))
    value2 = fields.Str(required=True)
    file_name = fields.Str(required=True)
