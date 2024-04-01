import json
from HW_15.test.conftest import user_api, faker

import logging

from api_service.common.assertation.user_asserts import UserAsserts
from api_service.common.controllers import pet_api
from api_service.common.dtos.payload_pet import PetPayload
from api_service.common.dtos.payload_user import CreateUserPayload
from api_service.common.controllers.pet_api import PetsAPI
from api_service.common.dtos.responses.create_pet_dto import GetPetsSchema

logger = logging.getLogger(__file__)

pet_api = PetsAPI()


def test_add_pet():
    payload = PetPayload.random_pet().get_dict()
    pet_api.add_pet(body=json.dumps(payload, indent=4),
                    headers={"Content-Type": "application/json", "accept": "application/json"})


def test_find_pet_by_id():
    payload = PetPayload.random_pet().get_dict()
    id = payload['id']
    pet_api.add_pet(body=json.dumps(payload, indent=4),
                    headers={"Content-Type": "application/json", "accept": "application/json"})
    pet = pet_api.get_pet(id=id, headers={"Content-Type": "application/json", "accept": "application/json"})
    petDict = pet.get_dict()
    assert petDict['id'] == id


def test_update_pet_by_id():
    payload = PetPayload.random_pet().get_dict()
    id = payload['id']
    pet_api.add_pet(body=json.dumps(payload, indent=4),
                    headers={"Content-Type": "application/json", "accept": "application/json"})
    payload_update = {'name': faker.word(), 'status': faker.word()}

    result = pet_api.update_pet(id=id, body=payload_update,
                                headers={"Content-Type": "application/x-www-form-urlencoded",
                                         "accept": "application/json"})
    assert result['message'] == str(id)


def test_find_pets_by_status():
    response = pet_api.find_pets_by_status(params={"status": "available"})

    for el in response:
        assert el["status"] == "available"
