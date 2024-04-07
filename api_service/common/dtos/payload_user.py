import random
from faker import Faker
import time


class CreateUserPayload:
    faker = Faker()

    def __init__(self, id, username, firstName, lastName, email, password, phone, userStatus=0):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus

    @classmethod
    def random(cls, username=None, firstName=None, lastName=None, password=None, email=None, phone=None):
        return cls(
            id=int((time.time()) % 1000000),
            username=username or cls.faker.name(),
            firstName=firstName or cls.faker.name(),
            lastName=lastName or cls.faker.name(),
            email=email or cls.faker.email(),
            password=password or cls.faker.password(),
            phone=phone or cls.generate_random_phone_number()
        )

    def get_dict(self):
        return self.__dict__

    @staticmethod
    def generate_random_phone_number():
        return '+1' + ''.join(str(random.randint(0, 9)) for _ in range(10))
