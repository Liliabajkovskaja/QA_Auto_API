import random

import pytest
from faker import Faker

from api_service.common.controllers.users_api import UsersAPI
# from api_service import UsersAPI
#
faker = Faker()
user_api = UsersAPI()



# @pytest.fixture
# def delete_user_fixture(user_api):
#     yield
#     if hasattr(delete_user_fixture, 'username'):
#         user_api.delete_user(username=delete_user_fixture.username)
#         print(f'user  was deleted')






created_user = None

@pytest.fixture
def delete_user_fixture(request):
    global created_user
    yield
    if created_user:
        username = created_user['username']
        UsersAPI().delete_user(username)
        print(f'User {username} was deleted')
        created_user = None