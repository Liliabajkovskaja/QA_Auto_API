import pytest
from assertpy import assert_that

from core.assertations.db_users_asserts import assert_one_car
from core.db_base.sqlite_car_logistics_table import SqliteCarLogisticsTable
from test_db.conftest import create_delete_car
import allure


@pytest.mark.db_tests
@allure.title("Test Get all cars")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_get_all_cars():
    cars = SqliteCarLogisticsTable().get_all_cars()
    assert_that(cars).is_not_empty()
    for car in cars:
        assert_that(car[0]).is_greater_than(0)


@allure.title("Test Get car with id")
@pytest.mark.db_tests
def test_get_with_id_1():
    car_id = 1
    car = SqliteCarLogisticsTable().get_id_by_id(car_id)
    assert_that(car).is_length(1)
    car = car[0]
    assert_that(car[0]).is_equal_to(car_id)


@pytest.mark.db_tests
def test_get_info_created_car(create_delete_car):
    car = SqliteCarLogisticsTable().get_id_by_id(create_delete_car['car_id'])
    assert_one_car(db_data=car, expected_data=create_delete_car)


@allure.title("Test update car status")
@pytest.mark.db_tests
def test_update_car_status(create_delete_car):
    car_data = create_delete_car
    car_id = car_data["car_id"]
    allure.step(f'Check the initial car status')
    initial_car_status = SqliteCarLogisticsTable().get_id_by_id(car_id)[0][5]
    assert initial_car_status == 0
    allure.step(f'Update the car status')
    SqliteCarLogisticsTable().update_car_status(car_id)
    allure.step(f'Check that car status has been successfully updated to 1')
    updated_car_status = SqliteCarLogisticsTable().get_id_by_id(car_id)[0][5]
    assert updated_car_status == 1
