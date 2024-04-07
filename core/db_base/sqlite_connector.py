import sqlite3
from os.path import join

from utils.constants import ROOT_PATH
from utils.db_config_manager import DBConfigManager


class BaseSqliteConnector:

    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.conn = sqlite3.connect(database=self.file_path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


class SqliteConnector(BaseSqliteConnector):

    def __init__(self):
        super().__init__(DBConfigManager.sqlite_db_path)
