from datetime import datetime
import pandas as pd

from inmet_api.main import main_inmet as previsao
from maps_api.main import main_maps as rotas


df_previsao = previsao()
df_rotas = rotas()

df_rotas['data'] = datetime.now().date()

df_previsao['dia'] = pd.to_datetime(df_previsao['dia']).dt.date
df_rotas['data'] = pd.to_datetime(df_rotas['data']).dt.date

# Merge of dates (join previsao + rotas )
df_final = pd.merge(
    df_rotas,
    df_previsao,
    left_on='data',
    right_on='dia',
    how='left'
)

print('📊 Clima + Mobilidade Unificados:')
print(df_final)

df_final.to_csv('clima_mobilidade.csv', index=False)