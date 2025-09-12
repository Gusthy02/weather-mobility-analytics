from .config import CIDADE
from .dicionary import mapa_tempo, translate_codes
from .service import get_codigo_cidade, get_previsao_7dias

def calculate_prevision():
    """
    Calcula a previsão do tempo para a cidade configurada.

    1. Obtém o código da cidade usando a função `get_codigo_cidade`.
    2. Busca a previsão de 7 dias via função `get_previsao_7dias`.
    3. Traduz os códigos meteorológicos para descrições legíveis usando `translate_codes`.

    Returns:
        pd.DataFrame: DataFrame contendo a previsão de 7 dias com descrições legíveis.
    """
    codigo_sp = get_codigo_cidade(CIDADE)
    df_previsao = get_previsao_7dias(codigo_sp)
    df_previsao = translate_codes(mapa_tempo, df_previsao)
    return df_previsao

def main_inmet():
    """
    Função principal que exibe a previsão do tempo no console.

    1. Chama `calculate_prevision` para obter os dados.
    2. Imprime no console uma tabela com a previsão para os próximos 7 dias.
    
    Returns:
        pd.DataFrame: DataFrame contendo a previsão de 7 dias.
    """
    print("🔍 Buscando previsão...")

    df_previsao = calculate_prevision()

    print(f"\n🌦️ Previsão 7 dias - {CIDADE}/SP:")
    print(df_previsao)

    return df_previsao

if __name__ == "__main__":
    main_inmet()
