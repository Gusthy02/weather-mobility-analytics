<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=00A3D9&height=180&section=header&animation=twinkling"/>

# 🌦️ Weather & Mobility Analytics

![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-5.7-brightgreen?logo=mysql)
![License](https://img.shields.io/badge/license-MIT-green)

**Autor:** Gustavo Thyerris Nascimento Oliveira  
**Email:** gusthyerris@gmail.com  
**LinkedIn:** [https://www.linkedin.com/in/gustavo-thyerris/](https://www.linkedin.com/in/gustavo-thyerris/)  
**Celular:** +55 (11) 95655-1862  

---

## 🔹 Sobre o Projeto

O **Weather & Mobility Analytics** integra informações climáticas e de mobilidade urbana para analisar como o clima impacta o tempo de deslocamento.  

O projeto combina dados de APIs públicas, processamento de dados em Python e armazenamento em MySQL, possibilitando insights sobre trajetos e planejamento urbano.  

📊 **Áreas de aplicação:** Data Analytics, Data Science, BI, Urban Mobility.

![Banner](https://raw.githubusercontent.com/Gusthy02/weather-mobility-analytics/main/docs/banner.png)

---

## 🔹 Tecnologias Utilizadas

- **Python 3.10+**  
- **Pandas**: manipulação e análise de dados  
- **Requests**: integração com APIs externas  
- **MySQL**: armazenamento de dados históricos  
- **Matplotlib**: gráficos e visualizações  
- **dotenv**: variáveis de ambiente  
- **Google Cloud Plataform**: variáveis de ambiente  
- **APIs**:
  - INMET/CPTEC: previsão do tempo 7 dias  
  - Google Maps Directions API: rotas e tempo de deslocamento  

![Tech Stack](https://raw.githubusercontent.com/Gusthy02/weather-mobility-analytics/main/docs/tech_stack.png)

---

## 🔹 Funcionalidades

- ✅ Consulta previsão do tempo via INMET  
- ✅ Consulta rotas de transporte via Google Maps API  
- ✅ Normalização e merge dos dados  
- ✅ Armazenamento em MySQL  
- ✅ Exportação em CSV e Excel  
- ✅ Visualização e análise da relação clima x mobilidade  

![Workflow](https://raw.githubusercontent.com/Gusthy02/weather-mobility-analytics/main/docs/workflow.png)

---

## 🔹 Como Funciona

O projeto segue o padrão **ETL (Extract, Transform, Load)**:

1. **Extração (Extract)**  
   - Dados de clima e rotas via APIs  

2. **Transformação (Transform)**  
   - Normalização de datas, tradução de códigos meteorológicos e merge de tabelas  

3. **Carga (Load)**  
   - Armazenamento no MySQL  
   - Exportação em CSV e Excel  

4. **Visualização**  
   - Gráficos de tempo médio de deslocamento e temperatura máxima  
   - Identificação de padrões e correlações  

---

## 🔹 Instalação e Uso

### Pré-requisitos
- Python 3.10+  
- MySQL  
- Arquivo `.env` com variáveis:

```env
GOOGLE_API_KEY=your_google_maps_api_key
MYSQL_USER=seu_usuario
MYSQL_PASSWORD=sua_senha
MYSQL_HOST=localhost
MYSQL_DB=nome_do_banco
```

### Instalação Linux
```env
git clone https://github.com/Gusthy02/weather-mobility-analytics.git

cd weather-mobility-analytics

python -m venv venv

Source venv/bin/activate  # Linux/macOS

pip install -r requirements.txt
```
### Instalação Windows
```env
git clone https://github.com/Gusthy02/weather-mobility-analytics.git

cd weather-mobility-analytics

python -m venv venv

venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

## 🔹 Execução

### Instalação Windows
    python -m process_data.export_data

### Instalação Windows
    python -m mysql_db.data_visualisation

### Instalação Windows
    python -m process_data.main

## 🔹 Exemplos de Insights

- Como o clima impacta o tempo médio de deslocamento

- Correlação entre chuva e aumento de tempo de viagem

- Rotas mais rápidas em diferentes condições climáticas

- Base para dashboards de planejamento urbano

## 🔹 Estrutura do Projeto

```
weather-mobility-analytics/
├── inmet_api/            # API de previsão do tempo
├── maps_api/             # API de rotas do Google Maps
├── process_data/         # Normalização, merge e exportação de dados
├── mysql_db/             # Conexão, carga e visualização no MySQL
├── env/                  # Variáveis de ambiente
├── final_data/           # Exportação de CSV/Excel
├── docs/                 # Imagens de exemplo e workflow
├── requirements.txt      # Dependências Python
└── README.md             # Documentação do projeto

```

## 🔹 Contato

### Gustavo Thyerris Nascimento Oliveira

- 📧 Email: gusthyerris@gmail.com
- 💼 LinkedIn: https://www.linkedin.com/in/gustavo-thyerris/
- 📱 Celular: +55 (11) 95655-1862
