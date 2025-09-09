import requests
import pandas as pd

# ================================
# 2️⃣ Dados de mobilidade (Google Maps Transit)
# ================================

TOKEN = 'AIzaSyAdkan_ejDqlCA-3M_jFwRpVc-qO_nLIFI'
origin = 'Avenida Paulista, São Paulo'
destination = 'Pinheiros, São Paulo'

url_maps = (
    f'https://maps.googleapis.com/maps/api/directions/json'
    f'?origin={origin}&destination={destination}&mode=transit&key={TOKEN}'
)

response = requests.get(url_maps)
data = response.json()

if data['status'] != 'OK':
    print('❌ Erro Google Maps:', data.get('error_message'))

routes_info = []
for route in data.get('routes', []):
    for leg in route.get('legs', []):
        routes_info.append({
            'start_address': leg['start_address'],
            'end_address': leg['end_address'],
            'duration_text': leg['duration']['text'],
            'duration_value': leg['duration']['value'],
            'distance_text': leg['distance']['text'],
            'distance_value': leg['distance']['value'],
        })

df_routes = pd.DataFrame(routes_info)
print("\n🚌 Rotas de Transporte Público - Google Maps:")
print(df_routes)