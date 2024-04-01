from marshmallow import Schema, fields, post_load, validate
from dataclasses import dataclass

@dataclass
class GetUserDTO:
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: str
    def get_dict(self):
        return self.__dict__
class GetUserSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    firstName = fields.Str(required=True)
    lastName = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    phone = fields.Str(required=True)
    userStatus = fields.Int(required=True)

    @post_load
    def get_object(self, data, **kwargs):
        return GetUserDTO(**data)



