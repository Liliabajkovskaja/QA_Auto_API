import random
from faker import Faker


class Category:
    faker = Faker()

    def __init__(self, id=None, name=None):
        self.id = id or random.randint(1, 10000)
        self.name = name or self.faker.word()

    def get_dict(self):
        return {"id": self.id, "name": self.name}


class Tag:
    faker = Faker()

    def __init__(self, id=None, name=None):
        self.id = id or random.randint(1, 10000)
        self.name = name or self.faker.word()

    def get_dict(self):
        return {"id": self.id, "name": self.name}


class PetPayload:
    faker = Faker()

    def __init__(self, id=None, category=None, name=None, photo_urls=None, tags=None, status=None):
        self.id = id
        self.category = category
        self.name = name
        self.photo_urls = photo_urls
        self.tags = tags
        self.status = status

    @classmethod
    def random_pet(cls, id=None, category=None, name=None, photo_urls=None, tags=None, status=None):
        return cls(
            id=id or random.randint(1, 10000),
            category=category or Category(),
            name=name or cls.faker.word(),
            photo_urls=photo_urls or [cls.faker.image_url()],
            tags=tags or [Tag()],
            status=status or cls.faker.random_element(elements=("available", "pending", "sold"))
        )

    def get_dict(self):
        return {
            "id": self.id,
            "category": self.category.get_dict(),
            "name": self.name,
            "photoUrls": self.photo_urls,
            "tags": [tag.get_dict() for tag in self.tags],
            "status": self.status
        }
