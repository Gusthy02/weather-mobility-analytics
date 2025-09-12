from process_data.process_api_datas import normalizate_data, merge_data

def main_process_data():
    # normalizate data
    df_previsao, df_rotas = normalizate_data()

    # merge data
    df_final = merge_data(df_previsao, df_rotas)

    return df_final

if __name__ == "__main__":
    main_process_data()