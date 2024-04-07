# import sqlite3
#
# sqlite_create_db = """
# CREATE TABLE IF NOT EXISTS CarLogistics (
# car_id INTEGER PRIMARY KEY,
# model TEXT,
# driver_name TEXT,
# vin INTEGER,
# payload_capacity INTEGER,
# car_status INTEGER,
# fact_trip INTEGER,
# plan_trip INTEGER
# );
#
# """
#
# if __name__ == '__main__':
#     conn = sqlite3.connect(database='test_db.db')
#     cursor = conn.cursor()
#     cursor.execute(sqlite_create_db)
#
#     cursor.execute('INSERT INTO CarLogistics VALUES (1, "Audi", "Ali Mustafa", 874209753, 1500, 1, 2121, 1501)')
#     conn.commit()
#     print(cursor.execute('select * from CarLogistics').fetchall())
#     cursor.close()
#     conn.close()