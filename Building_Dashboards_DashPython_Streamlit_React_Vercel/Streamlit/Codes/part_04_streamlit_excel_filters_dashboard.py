import streamlit as st
import pandas as pd
import numpy as np


df1=pd.read_excel("BASE01.CREDITO.xlsx")
df2=pd.read_excel("BASE02.CREDITO.xlsx")
df=df1


st.title("Layout: Sidebar, Colunas e Abas")

# SIDEBAR
st.sidebar.header("Filtros")
with st.sidebar:
    #idade_min, idade_max = (\
    #int(df["idade"].min()), int(df["idade"].max())) \
    #if "idade" in df else (0, 0)
    idade_min=df["idade"].min()
    idade_max=df["idade"].max()
    idade_sel = st.slider(\
        "Faixa de idade", idade_min, idade_max,\
        (idade_min, idade_max), step=1)
    regiao=st.selectbox(\
        "Região",options=df["regiao"].unique())
    base=st.radio("BASE",options=[1,2])


if base==1:
    df=df1
else:
    df=df2
    
dfMediaSexo=df[["sexo","valorcredito"]].groupby(by=["sexo"]).sum().reset_index()

# ABAS
st.write("Filtrado pela região "+regiao)
aba1, aba2,aba3 = st.tabs(["Tabela", \
                          "Estatísticas","Gráfico"])
with aba1:
    fdf = df[(df["idade"] >= idade_sel[0]) \
             & (df["idade"] <= idade_sel[1])]
    fdf=fdf[fdf["regiao"]==regiao]
    st.dataframe(fdf)
with aba2:
    fdf = df[(df["idade"] >= idade_sel[0]) \
             & (df["idade"] <= idade_sel[1])]
    fdf=fdf[fdf["regiao"]==regiao]
    st.write(fdf.describe())
with aba3:
    fdf = df[(df["idade"] >= idade_sel[0]) \
             & (df["idade"] <= idade_sel[1])]
    fdf=fdf[fdf["regiao"]==regiao]
    dfMediaSexo=fdf[["sexo","valorcredito"]].\
    groupby(by=["sexo"]).sum().reset_index()
    st.bar_chart(data=dfMediaSexo,\
                  x="sexo",y="valorcredito")