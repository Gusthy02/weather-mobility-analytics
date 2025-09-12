from process_data.process_api_datas import normalizate_data, merge_data

def main_process_data():
    """
    Função principal para processar e unir os dados de previsão do tempo e rotas.

    Fluxo:
        1. Normaliza os dados (previsão do tempo e rotas de transporte).
        2. Realiza o merge entre os dois DataFrames usando a data como chave.
        3. Retorna o DataFrame final consolidado.

    Returns:
        pd.DataFrame: DataFrame final com informações combinadas de clima e mobilidade.
    """
    # Normaliza os dados
    df_previsao, df_rotas = normalizate_data()

    # Merge dos dados
    df_final = merge_data(df_previsao, df_rotas)

    return df_final

if __name__ == "__main__":
    main_process_data()
