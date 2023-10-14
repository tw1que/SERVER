from marshmallow import Schema, fields, validate

class DentistsSchema(Schema):
    id = fields.Integer(dump_only=True)
    initials = fields.String(required=True, validate=validate.Length(min=1))
    first_name = fields.String()
    last_name = fields.String(required=True, validate=validate.Length(min=1))
