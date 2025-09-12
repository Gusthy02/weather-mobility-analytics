import os
from process_data.main import main_process_data

def export_api_datas():
    """
    Exporta os dados processados para arquivos CSV e Excel na pasta 'final_data'.

    Fluxo:
        1. Define os caminhos das pastas e arquivos.
        2. Cria a pasta 'final_data' caso não exista.
        3. Salva o DataFrame final em CSV e Excel.

    Arquivos gerados:
        - final_data/clima_mobilidade.csv
        - final_data/clima_mobilidade.xlsx
    """
    # Caminhos das pastas
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = os.path.dirname(BASE_DIR)
    DATA_DIR = os.path.join(ROOT_DIR, "final_data")

    # Cria a pasta se não existir
    os.makedirs(DATA_DIR, exist_ok=True)

    # Caminhos dos arquivos
    csv_path = os.path.join(DATA_DIR, 'clima_mobilidade.csv')
    xlms_path = os.path.join(DATA_DIR, 'clima_mobilidade.xlsx')

    # Obtém os dados processados
    df_final = main_process_data()

    # Salva em CSV
    df_final.to_csv(csv_path, index=False)

    # Salva em Excel
    df_final.to_excel(xlms_path, index=False)
