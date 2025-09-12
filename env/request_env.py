from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Chave da API do Google Maps
api_key = os.getenv('GOOGLE_API_KEY')

# Credenciais do banco de dados MySQL
db_user = os.getenv('MYSQL_USER')
db_password = os.getenv('MYSQL_PASSWORD')
db_host = os.getenv('MYSQL_HOST')
db = os.getenv('MYSQL_DB')

"""
Este módulo centraliza a leitura das variáveis de ambiente necessárias para o projeto:

Variáveis esperadas no arquivo .env:
    - GOOGLE_API_KEY: chave da API do Google Maps
    - MYSQL_USER: usuário do MySQL
    - MYSQL_PASSWORD: senha do MySQL
    - MYSQL_HOST: host do MySQL
    - MYSQL_DB: nome do banco de dados MySQL

Observação:
    - Certifique-se de que o arquivo .env esteja presente na raiz do projeto.
    - Evite versionar o arquivo .env para proteger credenciais sensíveis.
"""
