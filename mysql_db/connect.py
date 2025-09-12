import mysql.connector

from .config import CREDENTIALS

def connect_with_database():
    conn = mysql.connector.connect(
        host = CREDENTIALS["host"],
        user = CREDENTIALS["user"],
        password = CREDENTIALS["password"],
        database = CREDENTIALS["database"]
    )
    return conn