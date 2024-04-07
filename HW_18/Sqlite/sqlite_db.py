import sqlite3

sqlite_create_db = """
CREATE TABLE IF NOT EXISTS CarLogistics (
car_id INTEGER PRIMARY KEY,
model TEXT,
driver_name TEXT,
vin INTEGER,
payload_capacity INTEGER,
car_status INTEGER,
fact_trip INTEGER,
plan_trip INTEGER
);

"""

# data = [
#     (1, 'Toyota', 'John Doe', 123456789, 1000, 1, 10, 15),
#     (2, 'Honda', 'Jane Doe', 987654321, 800, 1, 8, 12),
#     (3, 'Ford', 'Bob Smith', 246813579, 1200, 0, 5, 10),
#     (4, 'Chevrolet', 'Alice Johnson', 135792468, 1500, 1, 12, 20),
#     (5, 'Tesla', 'Charlie Brown', 864209753, 500, 0, 3, 7)
# ]

if __name__ == '__main__':
    conn = sqlite3.connect(database='test_sqlite_db.db')
    cursor = conn.cursor()
    # cursor.execute(sqlite_create_db)
    # cursor.executemany('INSERT INTO CarLogistics VALUES (?, ?, ?, ?, ?, ?, ?, ?)', data)
    # conn.commit()
    print(cursor.execute('select * from CarLogistics').fetchall())
    cursor.close()
    conn.close()
