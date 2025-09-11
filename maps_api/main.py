from .config import URL_MAPS
from .service import connect_with_api, extract_data

def calculate_routes():
    isConnected, data = connect_with_api(URL_MAPS)

    if isConnected is True:
        df_rotas = extract_data(data)

        return df_rotas
    
    return None

def main_maps():
    
    print("🔍 Calculando rotas...")
    
    df_rotas = calculate_routes()

    if df_rotas is not None:
        print(f"🚗 Informações da rota:")
        print(df_rotas)

    return df_rotas

if __name__ == "__main__":
    main_maps()