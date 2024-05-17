import allure
import pytest
from assertpy import assert_that

from core.db_base.sqlite_car_logistics_table import SqliteCarLogisticsTable


@allure.title("negative test_db get info nonexistent car")
@pytest.mark.db_tests
def test_get_info_nonexistent_car():
    car_id = 999999
    car = SqliteCarLogisticsTable().get_id_by_id(car_id)
    assert_that(car).is_empty()


@allure.title("negative test_db delete nonexistent car")
@pytest.mark.db_tests
def test_delete_nonexistent_car():
    car_id = 999999
    assert_that(SqliteCarLogisticsTable().delete_car_by_id(car_id)).is_false()
