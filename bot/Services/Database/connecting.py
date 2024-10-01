import psycopg2
from psycopg2 import connect
# from dotenv import load_dotenv
from bot.bot import config_dict
import os

from tests.postgresql_tests import cursor

# load_dotenv()

conn = psycopg2.connect(
    host=config_dict["DB_HOST"],
    user=config_dict["DB_USER"],
    password=config_dict["DB_PASS"],
    database=config_dict["DB_NAME"]
)
cursor = conn.cursor()

# class DataBaseApi:
#     def __init__(self):
#         self.connect: connect = None
#         self.cursor: connect().cursor() = None
#         self.connecting()
#         self.create_tables_if_not_exist()
#
#     def connecting(self):
#         self.connection = psycopg2.connect(
#             host=config_dict["DB_HOST"],
#             user=config_dict["DB_USER"],
#             password=config_dict["DB_PASS"],
#             database=config_dict["DB_NAME"]
#         )
#         self.cursor = self.connection.cursor()
#
#     def create_tables_if_not_exist(self):
#         self.cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             user_id INTEGER PRIMARY KEY,
#             username TEXT,
#             name TEXT
#         )
#         """)
#         self.connect.commit()
#
# database = DataBaseApi()




