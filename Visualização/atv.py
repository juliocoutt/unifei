import streamlit as st

# Importa as funções de cada módulo do projeto
from data_loader import load_data       # Carregamento e tratamento do CSV
from filtros import aplicar_filtros     # Filtros interativos da barra lateral
from graficos import grafico_linha, grafico_barras, grafico_dispersao, grafico_pizza  # Gráficos

# Configuração da página: layout largo e barra lateral aberta por padrão
st.set_page_config(page_title="Dashboard de Vendas de Café", layout="wide", initial_sidebar_state="expanded")

# Carrega os dados do CSV e aplica os filtros selecionados na barra lateral
df = load_data("coffee.csv")
dff = aplicar_filtros(df)

# CSS para reduzir o espaço superior, o tamanho do título e as fontes da barra lateral
st.markdown("""
    <style>
        .block-container { padding-top: 1.5rem; padding-bottom: 0rem; }
        h1 { font-size: 1.4rem !important; margin-bottom: 0rem !important; }
        section[data-testid="stSidebar"] * { font-size: 0.8rem !important; }
        section[data-testid="stSidebar"] h2 { font-size: 0.95rem !important; }
    </style>
""", unsafe_allow_html=True)

st.title("☕ Dashboard de Vendas de Café")

# Cria as duas abas: Gráficos e Tabela de Dados
aba_graficos, aba_tabela = st.tabs(["Gráficos", "Tabela de Dados"])

with aba_graficos:
    # Primeira linha: gráfico de linha e gráfico de barras
    col1, col2 = st.columns(2)
    with col1:
        grafico_linha(dff)
    with col2:
        grafico_barras(dff)

    # Segunda linha: gráfico de dispersão e gráfico de pizza
    col3, col4 = st.columns(2)
    with col3:
        grafico_dispersao(dff)
    with col4:
        grafico_pizza(dff)

with aba_tabela:
    # Exibe o DataFrame filtrado como tabela interativa
    st.subheader("Visualização dos Dados")
    st.dataframe(dff, use_container_width=True, height=600)
