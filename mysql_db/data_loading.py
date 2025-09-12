from mysql.connector import Error
import pandas as pd

from .connect import connect_with_database

def load_data_mysql(df_final):
    try:
        conn = connect_with_database()

        if conn.is_connected():
            print("✅ Conectado ao MySQL")

            df_main = pd.read_csv(df_final)

            cursor = conn.cursor()

            # Creating table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clima_mobilidade (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    start_address VARCHAR(255) NOT NULL,
                    end_address VARCHAR(255) NOT NULL,
                    duration_text VARCHAR(50),
                    duration_value INT,
                    distance_text VARCHAR(50)
                    distance_value INT,
                    data DATE,
                    tempo VARCHAR(10),
                    maxima INT,
                    minima INT,
                    iuv FLOAT    
                )
            """)

            # Insertind datas of dt_main
            for _, row in df_main.iterrows():
                cursor.execute("""
                    INSERT INTO clima_mobilidade
                        (start_address, end_address, duration_text, duration_value, distance_text, distance_value, data, tempo, maxima, minima, iuv)
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    row['start_address'],
                    row['end_address'],
                    row['duration_text'],
                    row['duration_value'],
                    row['distance_text'],
                    row['distance_value'],
                    row['data'],
                    row['tempo'],
                    row['maxima'],
                    row['minima'],
                    row['iuv']
                ))

            conn.commit()
            print("📁 Dados carregados no MySQL com sucesso!")

    except Error as e:
        print("❌ Erro ao conectar:", e)

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()