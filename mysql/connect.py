import mysql.connector
from mysql.connector import Error

from .config import CREDENTIALS

CONN = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senha123',
    database='etl_mobilidade'
)