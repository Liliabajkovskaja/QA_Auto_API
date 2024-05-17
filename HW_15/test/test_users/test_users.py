import json
import time

import pytest

from HW_15.test.conftest import user_api
from api_service.common.controllers.users_api import UsersAPI
from api_service.common.dtos.payload_user import CreateUserPayload





@pytest.mark.smoke
def test_create_user():

    payload = CreateUserPayload.random().get_dict()
    response = UsersAPI().create_user(body=json.dumps(payload, indent=4),
                                      headers={"Content-Type": "application/json", "accept": "application/json",
                                               "User-Agent": "PostmanRuntime/7.37.0"})
    global created_user

    assert response["message"] == str(payload["id"])
    created_user = payload

@pytest.mark.smoke
def test_delete_user():
    payload = CreateUserPayload.random().get_dict()
    username = payload["username"]
    user_api.create_user(body=json.dumps(payload, indent=4),
                         headers={"Content-Type": "application/json", "accept": "application/json",
                                  "User-Agent": "PostmanRuntime/7.37.0"})
    response = user_api.delete_user(username=username)
    assert response["message"] == username


def test_update_user():
    payload_create = CreateUserPayload.random().get_dict()
    user_api.create_user(body=json.dumps(payload_create, indent=4),
                         headers={"Content-Type": "application/json", "accept": "application/json",
                                  "User-Agent": "PostmanRuntime/7.37.0"})
    username = payload_create["username"]
    payload_update = CreateUserPayload.random().get_dict()

    response_update = user_api.update_user(username=username, body=json.dumps(payload_update),
                                           headers={"Content-Type": "application/json"})
    assert int(response_update["message"]) > payload_create["id"]
    user_api.delete_user(username=username)


def test_get_user_by_user_name():
    payload = CreateUserPayload.random().get_dict()
    json_data = json.dumps(payload, indent=4)
    time.sleep(1)
    user_api.create_user(body=json_data, headers={"Content-Type": "application/json", "accept": "application/json"})
    username = payload["username"]
    response = (user_api.get_user_by_user_name(username=username))
    assert payload == response.get_dict()
    user_api.delete_user(username=username)

@pytest.mark.smoke
def test_login_user():
    user_api.login()

@pytest.mark.smoke
def test_logout_user():
    user_api.login()
    user_api.logout()
