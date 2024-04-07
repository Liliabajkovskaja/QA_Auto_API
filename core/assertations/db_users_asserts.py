from assertpy import assert_that, soft_assertions


def assert_one_car(db_data: tuple, expected_data: dict):
    assert_that(db_data).is_length(1)
    car = db_data[0]

    with soft_assertions():
        assert_that(car[0]).is_equal_to(expected_data['car_id'])
        assert_that(car[1]).is_equal_to(expected_data['model'])
        assert_that(car[2]).is_equal_to(expected_data['driver_name'])
        assert_that(car[3]).is_equal_to(expected_data['vin'])
        assert_that(car[4]).is_equal_to(expected_data['payload_capacity'])
        assert_that(car[5]).is_equal_to(expected_data['car_status'])
        assert_that(car[6]).is_equal_to(expected_data['fact_trip'])
        assert_that(car[7]).is_equal_to(expected_data['plan_trip'])
