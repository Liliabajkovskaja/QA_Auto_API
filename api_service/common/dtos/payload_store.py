import random
from datetime import datetime

from faker import Faker


class StorePayload:
    faker = Faker()

    def __init__(self, id=None, petId=None, quantity=None, shipDate=None, complete=None, status=None):
        self.id = id
        self.petId = petId
        self.quantity = quantity
        self.shipDate = shipDate
        self.complete = complete
        self.status = status

    @classmethod
    def random_order(cls, id=None, petId=None, quantity=None, shipDate=None, complete=None, status=None):
        return cls(
            id=id or random.randint(1, 10),
            petId=petId or random.randint(1, 10000),
            quantity=quantity or random.randint(1, 10),
            shipDate=shipDate or datetime.now().replace(microsecond=0).isoformat(),
            complete=complete or False,
            status=status or cls.faker.random_element(elements=("placed", "completed", "cancelled"))
        )

    def get_dict(self):
        return {
            "id": self.id,
            "petId": self.petId,
            "quantity": self.quantity,
            "shipDate": self.shipDate,
            "complete": self.complete,
            "status": self.status
        }
