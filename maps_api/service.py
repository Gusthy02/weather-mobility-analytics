import requests    
import pandas as pd

def connect_with_api(URL_MAPS):
    '''
        Connect with the API and return error message.
    '''

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
    '''
        extract datas on the API and return in DataFrame format.
    '''

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