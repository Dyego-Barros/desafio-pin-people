import streamlit as st
import requests
import pandas as pd

# URLs dos seus endpoints
LIKERT_URL = "http://api:8000/funcionario/analise/likert"
FAVORABILIDADE_URL = "http://api:8000/funcionario/analise/favorabilidade"
ENPS_URL = "http://api:8000/funcionario/analise/enps"
st.set_page_config(page_title="Dashboard de Engajamento", layout="wide")
st.title("Dashboard de Engajamento, Favorabilidade e eNPS")

# --------------------------------------
# Buscar dados dos endpoints
# --------------------------------------
@st.cache_data(ttl=300)
def buscar_dados(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Erro ao buscar dados: {e}")
        return {}

likert_data = buscar_dados(LIKERT_URL)
favorabilidade_data = buscar_dados(FAVORABILIDADE_URL)
enps_data = buscar_dados(ENPS_URL)

# --------------------------------------
# Dashboard Likert
# --------------------------------------
st.header("Distribuição Likert (%) por Coluna")
for coluna, dados in likert_data.get("likert", {}).items():
    st.subheader(coluna.replace("_", " ").capitalize())
    likert_pct = dados.get("likert_pct", {})
    total_respostas = dados.get("total_respostas", 0)

    df = pd.DataFrame({
        "Nota": list(likert_pct.keys()),
        "Porcentagem": list(likert_pct.values())
    })

    st.bar_chart(df.set_index("Nota"))
    st.caption(f"Total de respostas: {total_respostas}")

# --------------------------------------
# Dashboard Favorabilidade
# --------------------------------------
st.header("Favorabilidade (%) por Coluna")
for coluna, dados in favorabilidade_data.get("favorabilidade", {}).items():
    st.subheader(coluna.replace("_", " ").capitalize())
    fav = dados.get("favorabilidade", {})

    df = pd.DataFrame({
        "Tipo": ["Favorável", "Neutro", "Desfavorável"],
        "Porcentagem": [fav.get("favoravel", 0), fav.get("neutro", 0), fav.get("desfavoravel", 0)]
    })

    st.bar_chart(df.set_index("Tipo"))

# --------------------------------------
# Dashboard eNPS
# --------------------------------------
st.header("eNPS")

enps_data = enps_data.get('enps', '')

total_respostas = int(enps_data.get("total_respostas", 0))
promotores = int(enps_data.get("promotores", 0))
neutros = int(enps_data.get("neutros", 0))
detratores = int(enps_data.get("detratores", 0))
score_enps = enps_data

st.caption(f"Total de respostas: {total_respostas}")

# -------------------------------
# Gráfico
# -------------------------------
import matplotlib.pyplot as plt
import pandas as pd

df_enps = pd.DataFrame({
    "Tipo": ["Promotores (9-10)", "Neutros (7-8)", "Detratores (0-6)"],
    "Quantidade": [promotores, neutros, detratores]
})

# 🚨 PROTEÇÃO CONTRA DADOS ZERADOS
if df_enps["Quantidade"].sum() == 0:
    st.warning("Ainda não há dados suficientes para gerar o gráfico de eNPS.")
else:
    fig, ax = plt.subplots()

    ax.pie(
        df_enps["Quantidade"],
        labels=df_enps["Tipo"],
        autopct="%1.1f%%",
        startangle=90
    )
    ax.axis("equal")

    st.pyplot(fig)
