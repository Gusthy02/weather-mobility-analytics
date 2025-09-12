from process_data.main import main_process_data
from process_data.export_data import export_api_datas

from mysql_db.data_loading import load_data_mysql

from mysql_db.data_visualisation import consult_data
from mysql_db.data_visualisation import ploting

def main_final():
    """
    Função principal do projeto que executa o fluxo completo de:
    
    1. Processamento dos dados brutos e integração de diferentes fontes.
    2. Exportação dos dados processados via API.
    3. Armazenamento dos dados finais em um banco MySQL.
    4. Consulta dos dados armazenados para análise.
    5. Visualização gráfica dos dados consultados.

    Esta função integra todas as etapas do pipeline de dados, garantindo
    que os dados processados estejam disponíveis para análise e visualização.
    """
    
    # Processa os dados brutos e gera o dataframe final
    df_final = main_process_data()
    
    # Exporta os dados processados para APIs externas ou arquivos
    export_api_datas()

    # Carrega os dados processados no banco de dados MySQL
    load_data_mysql(df_final)

    # Consulta os dados armazenados no MySQL para análise/visualização
    df_sql = consult_data()

    # Gera gráficos e visualizações a partir dos dados consultados
    ploting(df_sql)

# Executa a função principal se o script for rodado diretamente
if __name__ == "__main__":
    main_final()
