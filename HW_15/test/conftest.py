import random

import pytest
from faker import Faker

from api_service.common.controllers.users_api import UsersAPI

faker = Faker()
user_api = UsersAPI()


# @pytest.fixture
# def get_new_user_body():
#     user_name = faker.name()
#     first_name = faker.name()
#     last_name = faker.name()
#     email = faker.email()
#     password = faker.password()
#     phone = faker.phone_number()
#
#     return {
#         "id": 0,
#         "user_name": user_name,
#         "first_name": first_name,
#         "last_name": last_name,
#         "email": email,
#         "password": password,
#         "phone": phone,
#         "user_status": 0
#     }