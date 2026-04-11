import streamlit as st
import pandas as pd
import numpy as np

st.title("Layout: Sidebar, Colunas e Abas")

# SIDEBAR
st.sidebar.header("Filtros")
qtd = st.sidebar.slider("Quantidade de linhas", 10, 1000, 100)
#qtd=100
# Dados de exemplo
np.random.seed(42)
df = pd.DataFrame({
'categoria': np.random.choice(['A','B','C'], size=1000),
'valor': np.random.randn(1000).round(2),
'ano': np.random.choice([2022, 2023, 2024, 2025], size=1000)
})

# COLUNAS
dfAux=df[0:qtd]
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Registros", len(dfAux))
col2.metric("Média (valor)", f"{dfAux['valor'].mean():.2f}")
col3.metric("Desvio Padrão", f"{dfAux['valor'].std():.2f}")
col4.metric("Soma Padrão", f"{dfAux['valor'].sum():.2f}")

# ABAS
aba1, aba2 = st.tabs(["Tabela", "Estatísticas"])
with aba1:
    st.dataframe(df.head(qtd))
with aba2:
    dfAux=df[0:qtd]
    st.write(dfAux.describe())