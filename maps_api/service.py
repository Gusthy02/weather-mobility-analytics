import requests
import pandas as pd

def connect_with_api(URL_MAPS):
    """
    Conecta com a API do Google Maps Directions e verifica o status da resposta.

    Args:
        URL_MAPS (str): URL completa da requisição da API.

    Returns:
        tuple: (bool, dict or None)
            - True e os dados JSON se a conexão for bem-sucedida.
            - False e None se houver erro.
    """
    try:
        response = requests.get(URL_MAPS)
        data = response.json()

        if data['status'] == 'OK':
            print('✅ Conexão realizada com sucesso!')
            return True, data
        else:
            print('❌ Erro Google Maps:', data.get('error_message', 'Erro desconhecido'))
            return False, None
        
    except requests.exceptions.RequestException as e:
        print('❌ Erro na requisição:', str(e))
        return False, None

def extract_data(data):
    """
    Extrai informações relevantes da resposta da API e retorna em formato DataFrame.

    Args:
        data (dict): JSON retornado pela API do Google Maps Directions.

    Returns:
        pd.DataFrame: DataFrame com colunas:
            - start_address: Endereço de início da rota
            - end_address: Endereço de destino
            - duration_text: Duração em formato legível (ex: '15 mins')
            - duration_value: Duração em segundos
            - distance_text: Distância em formato legível (ex: '5 km')
            - distance_value: Distância em metros
    """
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
    return pd.DataFrame(routes_info)
