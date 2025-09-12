import os
from process_data.main import main_process_data

def export_api_datas():
    # caminho para a pasta
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = os.path.dirname(BASE_DIR)
    DATA_DIR = os.path.join(ROOT_DIR, "final_data")

    # confirma que a pasta existe
    os.makedirs(DATA_DIR, exist_ok = True)

    # salva o arquivo dentro da pasta
    csv_path = os.path.join(DATA_DIR, 'clima_mobilidade.csv')
    xlms_path = os.path.join(DATA_DIR, 'clima_mobilidade.xlsx')

    df_final = main_process_data()

    # save on csv
    df_final.to_csv(csv_path, index=False)

    # save on excel
    df_final.to_excel(xlms_path, index=False)
