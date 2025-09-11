import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import Error
import pandas as pd


# MySQL data consult
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senha123',
    database='etl_mobilidade'
)

query = 'SELECT data, AVG(duration_value/60) as tempo_medio_min, AVG(maxima) as temp_max FROM clima_mobilidade GROUP BY data'
df_sql = pd.read_sql(query, conn)

conn.close()

# ploting
plt.figure(figsize=(10, 5))
plt.plot(df_sql['data'], df_sql['tempo_medio_min'], marker='o', label='Tempo médio da viagem (min)')
plt.plot(df_sql['data'], df_sql['tempo_max'], marker='s', label='Temperatura máxima (°C)')
plt.legend()
plt.title('Relação entre clima e tempo de mobilidade')
plt.xlabel('Data')
plt.ylabel('valores')
plt.grid(True)
plt.show()