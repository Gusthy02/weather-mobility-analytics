from datetime import datetime
import pandas as pd

from inmet_api.main import main_inmet
from maps_api.main import main_maps

def normalizate_data():
    df_previsao = main_inmet()
    df_rotas = main_maps()

    df_rotas['data'] = datetime.now().date()

    df_previsao['dia'] = pd.to_datetime(df_previsao['dia']).dt.date
    df_rotas['data'] = pd.to_datetime(df_rotas['data']).dt.date

    return df_previsao, df_rotas

def merge_data(df_previsao, df_rotas):
    df_final = pd.merge(
        df_rotas,
        df_previsao,
        left_on='data',
        right_on='dia',
        how='left'
    )

    return df_final