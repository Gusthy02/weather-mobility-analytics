import requests
import xml.etree.ElementTree as ET
import pandas as pd

from .config import URL_LISTA_CIDADES, URL_PREVISAO

def get_codigo_cidade(cidade, uf="SP"):
    """
    Retorna o código da cidade com base no nome e estado (UF).

    Args:
        cidade (str): Nome da cidade a ser consultada.
        uf (str): Unidade federativa da cidade (default "SP").

    Returns:
        str: Código da cidade utilizado na API de previsão.

    Raises:
        ValueError: Se a cidade não for encontrada.
    """
    url = f"{URL_LISTA_CIDADES}?city={cidade}"
    response = requests.get(url)
    tree = ET.fromstring(response.content)

    cidades = [
        {
            "id": elem.find("id").text,
            "nome": elem.find("nome").text,
            "uf": elem.find("uf").text,
        }
        for elem in tree.findall("cidade")
    ]

    df_cidades = pd.DataFrame(cidades)
    df_filtrado = df_cidades[df_cidades["uf"] == uf]

    if df_filtrado.empty:
        raise ValueError(f"Cidade {cidade}/{uf} não encontrada")

    return df_filtrado.iloc[0]["id"]

def get_previsao_7dias(codigo_cidade):
    """
    Retorna a previsão do tempo para 7 dias de uma cidade específica.

    Args:
        codigo_cidade (str): Código da cidade obtido por `get_codigo_cidade`.

    Returns:
        pd.DataFrame: DataFrame com colunas ['dia', 'tempo', 'maxima', 'minima', 'iuv'].
    """
    url = URL_PREVISAO.format(codigo=codigo_cidade)
    response = requests.get(url)
    tree = ET.fromstring(response.content)

    previsoes = [
        {
            "dia": p.find("dia").text,
            "tempo": p.find("tempo").text,
            "maxima": int(p.find("maxima").text),
            "minima": int(p.find("minima").text),
            "iuv": float(p.find("iuv").text),
        }
        for p in tree.findall("previsao")
    ]

    return pd.DataFrame(previsoes)
