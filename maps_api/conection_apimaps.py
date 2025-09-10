import requests

def connect_with_api(TOKEN, ORIGIN, DESTINATION):
    try:
        url_maps = (
            f'https://maps.googleapis.com/maps/api/directions/json'
            f'?origin={ORIGIN}&destination={DESTINATION}&mode=transit&key={TOKEN}'
        )

        response = requests.get(url_maps)
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