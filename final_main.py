from process_data.main import main_process_data
from process_data.export_data import export_api_datas

from mysql_db.data_loading import load_data_mysql

from mysql_db.data_visualisation import consult_data
from mysql_db.data_visualisation import ploting

def main_final():
    # merge data
    df_final = main_process_data()
    export_api_datas()

    # save on mysql
    load_data_mysql(df_final)

    df_sql = consult_data()

    ploting(df_sql)

if __name__ == "__main__":
    main_final()