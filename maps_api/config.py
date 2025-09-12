from env.request_env import api_key

# Parâmetros da consulta de rotas
CREDENTIALS_AND_PARAMETERS = {
    'token': api_key,  # Chave da API do Google Maps
    'origin': 'Avenida Paulista, São Paulo',  # Endereço de origem
    'destination': 'Pinheiros, São Paulo'  # Endereço de destino
}

# Endpoint completo da API do Google Maps Directions
URL_MAPS = (
    f'https://maps.googleapis.com/maps/api/directions/json'
    f'?origin={CREDENTIALS_AND_PARAMETERS["origin"]}'
    f'&destination={CREDENTIALS_AND_PARAMETERS["destination"]}'
    f'&mode=transit'
    f'&key={CREDENTIALS_AND_PARAMETERS["token"]}'
)
