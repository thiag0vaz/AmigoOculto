from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(load_only=True, required=True)
    event_id = fields.Integer()
    amigo_oculto_id = fields.Integer(dump_only=True)
