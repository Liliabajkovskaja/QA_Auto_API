import allure
import pytest
from assertpy import assert_that

from core.assertations.db_users_asserts import assert_one_car
from core.db_base.sqlite_car_logistics_table import SqliteCarLogisticsTable
from test.db_tests.conftest import create_delete_car


@allure.title("negative test get info nonexistent car")
@pytest.mark.db_tests
def test_get_info_nonexistent_car():
    car_id = 999999
    car = SqliteCarLogisticsTable().get_id_by_id(car_id)
    assert_that(car).is_empty()


@allure.title("negative test delete nonexistent car")
@pytest.mark.db_tests
def test_delete_nonexistent_car():
    car_id = 999999
    assert_that(SqliteCarLogisticsTable().delete_car_by_id(car_id)).is_false()
