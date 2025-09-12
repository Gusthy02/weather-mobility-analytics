from request_env import api_key

# parameters to consult
CREDENTIALS_AND_PARAMETERS = {
    'token': api_key,
    'origin': 'Avenida Paulista, São Paulo',
    'destination': 'Pinheiros, São Paulo'
}

# endpoints
URL_MAPS = f'https://maps.googleapis.com/maps/api/directions/json?origin={CREDENTIALS_AND_PARAMETERS["origin"]}&destination={CREDENTIALS_AND_PARAMETERS["destination"]}&mode=transit&key={CREDENTIALS_AND_PARAMETERS["token"]}'
