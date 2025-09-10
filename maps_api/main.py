from config import URL_MAPS
from service import connect_with_api, extract_data

def main():
    
    print("🔍 Calculando rotas...")
    
    isConnected, data = connect_with_api(URL_MAPS)

    if isConnected is True:
        df_route = extract_data(data)


    print(f"🚗 Informações da rota:")
    print(df_route)

if __name__ == "__main__":
    main()