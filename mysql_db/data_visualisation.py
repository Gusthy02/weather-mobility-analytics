import matplotlib.pyplot as plt
import pandas as pd
from mysql.connector import Error

from .connect import connect_with_database

def consult_data():
    print('SUCESSO')

    try:
        conn = connect_with_database()

        if conn.is_connected():
            query = 'SELECT data, AVG(duration_value/60) as tempo_medio_min, AVG(maxima) as temp_max FROM clima_mobilidade GROUP BY data'
            df_sql = pd.read_sql(query, conn)

            return df_sql

    except Error as e:
        print("❌ Erro ao conectar:", e)

    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

# ploting
def ploting(df_sql):   
    print('SUCESSO')
    plt.figure(figsize=(10, 5))
    plt.plot(df_sql['data'], df_sql['tempo_medio_min'], marker='o', label='Tempo médio da viagem (min)')
    plt.plot(df_sql['data'], df_sql['tempo_max'], marker='s', label='Temperatura máxima (°C)')
    plt.legend()
    plt.title('Relação entre clima e tempo de mobilidade')
    plt.xlabel('Data')
    plt.ylabel('valores')
    plt.grid(True)
    plt.show()