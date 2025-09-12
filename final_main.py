from process_data.process_api_datas import normalizate_data
from process_data.process_api_datas import merge_data

from mysql_db.data_loading import load_data_mysql

from mysql_db.data_visualisation import consult_data
from mysql_db.data_visualisation import ploting

def main_final():
    # normalizate data
    df_previsao, df_rotas = normalizate_data()

    # merge data
    df_final = merge_data(df_previsao, df_rotas)

    # save on csv
    df_final.to_csv('clima_mobilidade.csv', index=False)

    # save on mysql
    load_data_mysql(df_final)

    df_sql = consult_data()

    ploting(df_sql)

if __name__ == "__main__":
    main_final()