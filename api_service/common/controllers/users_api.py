from api_service.base_api import BaseApi
from api_service.common.dtos.responses.get_user_dto import GetUserSchema, GetUserDTO


class UsersAPI:
    api_executor = BaseApi()
    base_url = "https://petstore.swagger.io/v2"
    create_user_url = f"{base_url}/user"
    user_login_url = f"{base_url}/user/login"
    user_logout_url = f"{base_url}/user/logout"

    def create_user(self, body: dict, headers=None):
        return self.api_executor.post(
            url=self.create_user_url,
            headers=headers,
            body=body,
            expected_status_code=200
        )

    def login(self):
        return self.api_executor.get(
            url=self.user_login_url,
            expected_status_code=200
        )

    def logout(self):
        return self.api_executor.get(
            url=self.user_logout_url,
            expected_status_code=200
        )

    def update_user(self, username: str, body: dict, headers=None):
        user_update_url = f"{self.base_url}/user/{username}"
        return self.api_executor.put(
            url=user_update_url,
            headers=headers,
            body=body,
            expected_status_code=200
        )

    def get_user_by_user_name(self, username: str, headers=None) -> GetUserDTO:
        get_user_by_user_name_url = f"{self.base_url}/user/{username}"
        return self.api_executor.get(
            url=get_user_by_user_name_url,
            headers=headers,
            expected_status_code=200,
            schema=GetUserSchema()
        )

    def delete_user(self, username: str, headers=None):
        get_user_by_user_name_url = f"{self.base_url}/user/{username}"
        return self.api_executor.delete(
            url=get_user_by_user_name_url,
            headers=headers,
            expected_status_code=200

        )
