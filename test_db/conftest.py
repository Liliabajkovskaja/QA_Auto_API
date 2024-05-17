from random import choice

import pytest

from core.db_base.sqlite_car_logistics_table import SqliteCarLogisticsTable


@pytest.fixture
def create_delete_car() -> dict:
    car_data = {
        "car_id": 3,
        "model": 'Honda',
        "driver_name": 'Jane Doe',
        "vin": 9999999999,
        "payload_capacity": 1500,
        "car_status": 0,
        "fact_trip": 400,
        "plan_trip": 500
    }
    SqliteCarLogisticsTable().create_car(**car_data)
    yield car_data
    SqliteCarLogisticsTable().delete_car_by_id(car_id=car_data['car_id'])
