from marshmallow import Schema, fields, post_load, validate
from dataclasses import dataclass


@dataclass
class CategoryDTO:
    id: int
    name: str

    def get_dict(self):
        return self.__dict__


@dataclass
class TagDTO:
    id: int
    name: str

    def get_dict(self):
        return self.__dict__


@dataclass
class PetsDTO:
    id: int
    category: CategoryDTO
    name: str
    photoUrls: list[str]
    tags: list[TagDTO]
    status: str
    def get_dict(self):
        return self.__dict__


class TagSchema(Schema):
    id = fields.Int(strict=True)
    name = fields.Str()

    @post_load
    def serialize(self, data, **kwarg):
        return TagDTO(**data)

class CategorySchema(Schema):
    id = fields.Int(strict=True)
    name = fields.Str()

    @post_load
    def serialize(self, data, **kwarg):
        return CategoryDTO(**data)


class GetPetsSchema(Schema):
    category = fields.Nested(CategorySchema(), default=None)
    id = fields.Int(required=True)
    name = fields.String()
    photoUrls = fields.List(fields.String())
    tags = fields.List(fields.Nested(TagSchema()))
    status = fields.String()

    @post_load
    def get_object(self, data, **kwargs):
        return PetsDTO(**data)

