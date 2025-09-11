import requests
import xml.etree.ElementTree as ET
import pandas as pd

from .config import URL_LISTA_CIDADES, URL_PREVISAO

def get_codigo_cidade(cidade, uf="SP"):

    """
    Returns the city code from the name.
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
    Returns the 7-day forecast in DataFrame format.
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