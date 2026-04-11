import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel("BASE01.CREDITO.xlsx")

df_media_sexo = (
    df[["sexo", "valorcredito"]]
    .groupby(by=["sexo"])
    .sum()
    .reset_index()
)

st.title("Layout: Sidebar, Colunas e Abas")


# ABAS
aba1, aba2, aba3, aba4 = st.tabs(
    ["Tabela", "Estatísticas", "Gráfico", "Pizza"]
)
with aba1:
    st.dataframe(df)
with aba2:
    st.write(df.describe())
with aba3:
    st.bar_chart(data=df_media_sexo, x="sexo", y="valorcredito")
with aba4:
    fig = px.pie(
        df_media_sexo,
        names="sexo",
        values="valorcredito",
        color_discrete_sequence=["red", "blue"],
    )
    st.plotly_chart(fig)
