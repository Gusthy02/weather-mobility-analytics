from datetime import datetime
import pandas as pd
from inmet_api.main import main_inmet
from maps_api.main import main_maps

def normalizate_data():
    """
    Normaliza os dados vindos das APIs de previsão do tempo e rotas de transporte.

    Fluxo:
        1. Obtém os dados da previsão do tempo via `main_inmet`.
        2. Obtém os dados das rotas via `main_maps`.
        3. Converte datas para o formato `datetime.date` para padronização.

    Returns:
        tuple: (df_previsao, df_rotas)
            - df_previsao: DataFrame com previsão do tempo.
            - df_rotas: DataFrame com informações das rotas.
    """
    df_previsao = main_inmet()
    df_rotas = main_maps()

    # Adiciona a coluna 'data' com a data atual para rotas
    df_rotas['data'] = datetime.now().date()

    # Converte datas para datetime.date
    df_previsao['dia'] = pd.to_datetime(df_previsao['dia']).dt.date
    df_rotas['data'] = pd.to_datetime(df_rotas['data']).dt.date

    return df_previsao, df_rotas

def merge_data(df_previsao, df_rotas):
    """
    Realiza o merge dos DataFrames de previsão do tempo e rotas com base na data.

    Args:
        df_previsao (pd.DataFrame): DataFrame da previsão do tempo.
        df_rotas (pd.DataFrame): DataFrame das rotas.

    Returns:
        pd.DataFrame: DataFrame consolidado com informações de clima e mobilidade.
    """
    df_final = pd.merge(
        df_rotas,
        df_previsao,
        left_on='data',
        right_on='dia',
        how='left'
    )

    return df_final
