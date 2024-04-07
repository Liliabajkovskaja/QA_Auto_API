from random import choice, random

from core.db_base.base_sqlite_table import execute_sql_query

import allure


class SqliteCarLogisticsTable:

    def __init__(self):
        self.db_name = 'test_db.db'
        self.table_name = 'CarLogistics'

    @allure.step
    @execute_sql_query
    def get_all_cars(self):
        return f'select * from {self.table_name}'

    @allure.step
    @execute_sql_query
    def get_id_by_id(self, car_id):
        return f'select * from {self.table_name} where car_id = {car_id}'

    @allure.step
    @execute_sql_query
    def create_car(self, car_id=None, model='Honda', driver_name='Jane Doe', vin=None, car_status=0,
                   payload_capacity=1500,
                   fact_trip=0, plan_trip=2):
        car_id = car_id or choice(range(2, 10000))
        vin = vin or choice(range(1000000, 9999999))
        fact_trip = fact_trip or choice(range(100, 200))
        plan_trip = plan_trip or choice(range(200, 500))

        return f'insert into {self.table_name} values ({car_id}, "{model}", "{driver_name}", {vin},{payload_capacity},{car_status},{fact_trip},{plan_trip})'

    @allure.step
    @execute_sql_query
    def delete_car_by_id(self, car_id):
        return f'delete from {self.table_name} where car_id = {car_id}'

    @allure.step
    @execute_sql_query
    def update_car_status(self, car_id):
        return f'update {self.table_name} set car_status = 1 where car_id = {car_id}'

#  print(SqliteUsersTable().get_all_cars)
# print(SqliteCarLogisticsTable().create_car)
