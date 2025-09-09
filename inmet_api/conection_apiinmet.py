import requests
import xml.etree.ElementTree as ET
import pandas as pd

from translation_dictionary import translate_codes, mapa_tempo

# ================================
# 1️⃣ Dados de clima (CPTEC/INPE)
# ================================

# Cidade: São Paulo/SP
cidade = "Sao Paulo"
url_cidade = f"http://servicos.cptec.inpe.br/XML/listaCidades?city={cidade}"
response = requests.get(url_cidade)
tree = ET.fromstring(response.content)

cidades = []
for elem in tree.findall("cidade"):
    cidades.append({
        "id": elem.find("id").text,
        "nome": elem.find("nome").text,
        "uf": elem.find("uf").text,
    })

df_cidades = pd.DataFrame(cidades)
df_sp = df_cidades[df_cidades["uf"] == "SP"]
codigo_sp = df_sp.iloc[0]["id"]

# Previsão 7 dias
url_previsao = f"http://servicos.cptec.inpe.br/XML/cidade/{codigo_sp}/previsao.xml?dias=7"
response = requests.get(url_previsao)
tree = ET.fromstring(response.content)

previsoes = []
for p in tree.findall("previsao"):
    previsoes.append({
        "dia": p.find("dia").text,
        "tempo": p.find("tempo").text,
        "maxima": int(p.find("maxima").text),
        "minima": int(p.find("minima").text),
        "iuv": float(p.find("iuv").text),
    })

df_previsao = pd.DataFrame(previsoes)

translate_codes(mapa_tempo, df_previsao)

print("🌦️ Previsão 7 dias - São Paulo/SP:")
print(df_previsao)