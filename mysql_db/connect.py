import mysql.connector
from .config import CREDENTIALS

def connect_with_database():
    """
    Cria uma conexão com o banco de dados MySQL usando as credenciais configuradas.

    Returns:
        mysql.connector.connection.MySQLConnection: Objeto de conexão com o MySQL.
    """
    conn = mysql.connector.connect(
        host=CREDENTIALS["host"],
        user=CREDENTIALS["user"],
        password=CREDENTIALS["password"],
        database=CREDENTIALS["database"]
    )
    return conn
