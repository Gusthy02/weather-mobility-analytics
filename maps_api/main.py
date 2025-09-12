from .config import URL_MAPS
from .service import connect_with_api, extract_data

def calculate_routes():
    """
    Calcula as rotas entre os endereços configurados usando a API do Google Maps.

    1. Conecta com a API via `connect_with_api`.
    2. Se a conexão for bem-sucedida, extrai os dados de rotas via `extract_data`.

    Returns:
        pd.DataFrame or None: DataFrame com informações das rotas, ou None se houver falha na API.
    """
    isConnected, data = connect_with_api(URL_MAPS)

    if isConnected:
        df_rotas = extract_data(data)
        return df_rotas
    
    return None

def main_maps():
    """
    Função principal para exibir no console as rotas calculadas.

    1. Chama `calculate_routes` para obter os dados das rotas.
    2. Imprime os detalhes das rotas se a consulta for bem-sucedida.

    Returns:
        pd.DataFrame or None: DataFrame com informações das rotas ou None.
    """
    print("🔍 Calculando rotas...")
    
    df_rotas = calculate_routes()

    if df_rotas is not None:
        print(f"🚗 Informações da rota:")
        print(df_rotas)

    return df_rotas

if __name__ == "__main__":
    main_maps()
