from .config import CIDADE
from .dictionary import mapa_tempo, translate_codes
from .service import get_codigo_cidade, get_previsao_7dias

def calculate_prevision():
    codigo_sp = get_codigo_cidade(CIDADE)

    df_previsao = get_previsao_7dias(codigo_sp)

    df_previsao = translate_codes(mapa_tempo, df_previsao)

    return df_previsao

def main_inmet():
    
    print("🔍 Buscando previsão...")

    df_previsao = calculate_prevision()

    print(f"\n🌦️ Previsão 7 dias - {CIDADE}/SP:")
    print(df_previsao)

    return df_previsao


if __name__ == "__main__":
    main_inmet()