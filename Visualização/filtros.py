import streamlit as st
import pandas as pd

def aplicar_filtros(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Filtros")

    # Extrai os anos disponíveis no dataset e cria o selectbox
    anos = ["Todos"] + sorted(df["data"].dt.year.dropna().unique().astype(str).tolist())
    ano_sel = st.sidebar.selectbox("Ano", anos, index=0)

    # Ordena os meses cronologicamente e exibe apenas os presentes no dataset
    ordem_meses = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
    meses_disp = df["nome_mes"].dropna().unique().tolist()
    meses_ord = [m for m in ordem_meses if m in meses_disp]
    mes_sel = st.sidebar.selectbox("Mês", ["Todos"] + meses_ord, index=0)

    # Ordena os dias da semana (Seg a Dom) e exibe apenas os presentes no dataset
    ordem_dias = ["Seg","Ter","Qua","Qui","Sex","Sáb","Dom"]
    dias_disp = df["dia_da_semana"].dropna().unique().tolist()
    dias_ord = [d for d in ordem_dias if d in dias_disp]
    dia_sel = st.sidebar.selectbox("Dia da Semana", ["Todos"] + dias_ord, index=0)

    # Copia o DataFrame original para não modificá-lo
    dff = df.copy()

    # Aplica cada filtro de forma cumulativa, caso não seja "Todos"
    if ano_sel != "Todos":
        dff = dff[dff["data"].dt.year.astype(str) == ano_sel]
    if mes_sel != "Todos":
        dff = dff[dff["nome_mes"] == mes_sel]
    if dia_sel != "Todos":
        dff = dff[dff["dia_da_semana"] == dia_sel]

    return dff
