import json
import logging

from api_service.common.controllers import store_api
from api_service.common.controllers.store_api import StoreAPI
from api_service.common.dtos.payload_store import StorePayload

logger = logging.getLogger(__file__)

store_api = StoreAPI()


def test_add_order():
    payload = StorePayload.random_order().get_dict()
    res = store_api.add_order(body=json.dumps(payload, indent=4),
                              headers={"Content-Type": "application/json", "accept": "application/json"})
    assert payload['id'] == res['id']


def test_find_order_by_id():
    payload = StorePayload.random_order().get_dict()
    id = payload['id']
    create_res = store_api.add_order(body=json.dumps(payload, indent=4),
                                     headers={"Content-Type": "application/json", "accept": "application/json"})
    find_res = store_api.get_order(id=id,
                                   headers={"accept": "application/json"})
    assert payload['id'] == find_res['id']


def test_delete_order_by_id():
    payload = StorePayload.random_order().get_dict()
    id = payload['id']
    store_api.add_order(body=json.dumps(payload, indent=4),
                        headers={"Content-Type": "application/json", "accept": "application/json"})
    find_res = store_api.delete_order(id=id,
                                      headers={"accept": "application/json"})
    assert str(payload['id']) == str(find_res['message'])
