# Dicionário para tradução dos códigos meteorológicos
mapa_tempo = {
    "ec": "Encoberto c/ Chuvas Isoladas",
    "ci": "Chuvas Isoladas",
    "c": "Chuva",
    "in": "Instável",
    "pp": "Possibilidade de Pancadas",
    "cm": "Chuva pela Manhã",
    "cn": "Chuva à Noite",
    "pt": "Pancadas de Chuva à Tarde",
    "pm": "Pancadas de Chuva pela Manhã",
    "np": "Nublado c/ Pancadas",
    "pc": "Pancadas de Chuva",
    "pn": "Parcialmente Nublado",
    "cv": "Chuvisco",
    "ch": "Chuvoso",
    "t": "Tempestade",
    "ps": "Predomínio de Sol",
    "e": "Encoberto",
    "n": "Nublado",
    "cl": "Céu Claro",
    "nv": "Nevoeiro",
    "g": "Geada",
    "ne": "Neve",
    "nd": "Não Definido",
    "pnt": "Pancadas à Noite",
    "psc": "Possibilidade de Chuva",
    "pcm": "Possibilidade de Chuva pela Manhã",
    "pct": "Possibilidade de Chuva à Tarde",
    "pcn": "Possibilidade de Chuva à Noite",
    "npt": "Nublado c/ Pancadas à Tarde",
    "npn": "Nublado c/ Pancadas à Noite",
    "ncn": "Nublado c/ Possibilidade de Chuva à Noite",
    "nct": "Nublado c/ Possibilidade de Chuva à Tarde",
    "ncm": "Nublado c/ Possibilidade de Chuva pela Manhã",
    "npm": "Nublado c/ Pancadas pela Manhã",
    "npp": "Nublado c/ Possibilidade de Pancadas",
    "vn": "Variação de Nebulosidade",
    "ct": "Chuva à Tarde",
    "ppn": "Possibilidade de Pancadas à Noite",
    "ppt": "Possibilidade de Pancadas à Tarde",
    "ppm": "Possibilidade de Pancadas pela Manhã",
}

def translate_codes(dicionary, df):
    """
    Traduz os códigos meteorológicos do DataFrame para descrições legíveis.

    Args:
        dicionary (dict): Dicionário de tradução (ex: mapa_tempo).
        df (pd.DataFrame): DataFrame contendo a coluna 'tempo' com os códigos.

    Returns:
        pd.DataFrame: DataFrame com nova coluna 'tempo_desc' contendo as descrições.
    """
    df["tempo_desc"] = df["tempo"].map(dicionary)
    return df
