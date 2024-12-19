from marshmallow import Schema, fields

class EventSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String()
    created_at = fields.DateTime(dump_only=True)
