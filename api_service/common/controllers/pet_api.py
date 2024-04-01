from api_service.base_api import BaseApi
from api_service.common.dtos.responses.create_pet_dto import GetPetsSchema, PetsDTO


class PetsAPI:
    api_executor = BaseApi()
    base_url = "https://petstore.swagger.io/v2"
    add_new_pet_url = f"{base_url}/pet"
    find_pets_by_status_url = f"{base_url}/pet/findByStatus"
    find_pet_by_id_url = f"{base_url}/pet/{id}"

    user_login_url = f"{base_url}/user/login"
    user_logout_url = f"{base_url}/user/logout"

    def find_pets_by_status(self, headers=None, params=None, schema=None):
        return self.api_executor.get(
            url=self.find_pets_by_status_url,
            headers=headers,
            expected_status_code=200,
            params=params,
            schema=schema
        )

    def add_pet(self, body: dict, headers=None):
        return self.api_executor.post(
            url=self.add_new_pet_url,
            headers=headers,
            body=body,
            expected_status_code=200
        )

    def get_pet(self, id: int, headers=None) -> PetsDTO:
        find_pet_by_id_url = f"{self.base_url}/pet/{id}"
        return self.api_executor.get(
            url=find_pet_by_id_url,
            headers=headers,
            expected_status_code=200,
            schema=GetPetsSchema()
        )

    def update_pet(self, id: int, body: dict, headers=None):
        update_pet_by_id_url = f"{self.base_url}/pet/{id}"
        return self.api_executor.post(
            url=update_pet_by_id_url,
            headers=headers,
            body=body,
            expected_status_code=200
        )
