import json
from marshmallow import Schema, fields, post_load, validate
from dataclasses import dataclass


@dataclass
class CategoryDTO:
    id: int
    name: str


@dataclass
class TagDTO:
    id: int
    name: str


@dataclass
class PetsDTO:
    id: int
    category: CategoryDTO
    name: str
    photoUrls: list[str]
    tags: list[TagDTO]
    status: str


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
    id = fields.Int(strict=True)
    name = fields.String()
    photoUrls = fields.List(fields.String())
    tags = fields.List(fields.Nested(TagSchema()))
    status = fields.String()

    @post_load
    def get_object(self, data, **kwargs):
        return PetsDTO(**data)


if __name__ == '__main__':
    with open('pets.json', 'r') as file:
        data = json.load(file)

    pets_dto = GetPetsSchema(many=True).load(data)

    for pet in pets_dto:
        tags = [tag.name for tag in pet.tags]
        print(pet.name, pet.category.name, tags)
