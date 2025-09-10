from conection_apimaps import connect_with_api
from return_apimaps import extract_data

credentials_and_parameters = {
    'TOKEN': 'AIzaSyAdkan_ejDqlCA-3M_jFwRpVc-qO_nLIFI',
    'ORIGIN': 'Avenida Paulista, São Paulo',
    'DESTINATION': 'Pinheiros, São Paulo'
}

isConnected, data = connect_with_api(credentials_and_parameters['TOKEN'], credentials_and_parameters['ORIGIN'], credentials_and_parameters['DESTINATION'])

if isConnected is True:
    df_public_transport_routes = extract_data(data)