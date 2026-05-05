import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def grafico_linha(dff: pd.DataFrame):
    # Verifica se as colunas necessárias existem e se há dados
    if {"data", "valor"}.issubset(dff.columns) and not dff.empty:
        dff_sorted = dff.sort_values("data")  # Ordena por data para traçar a linha corretamente
        fig, ax = plt.subplots(figsize=(5, 2.2))
        ax.plot(dff_sorted["data"], dff_sorted["valor"])
        ax.set_xlabel("Data", fontsize=8)
        ax.set_ylabel("Valor (R$)", fontsize=8)
        ax.set_title("Vendas ao longo do tempo", fontsize=9)
        ax.tick_params(axis="both", labelsize=7)
        fig.tight_layout()
        st.pyplot(fig, clear_figure=True, use_container_width=True)
    else:
        st.info("Sem dados para o período selecionado.")

def grafico_barras(dff: pd.DataFrame):
    # Verifica se as colunas necessárias existem e se há dados
    if {"nome_cafe", "valor"}.issubset(dff.columns) and not dff.empty:
        # Agrupa por produto, soma os valores e ordena do maior para o menor
        vendas_por_cafe = dff.groupby("nome_cafe")["valor"].sum().sort_values(ascending=False)

        # Verifica se o resultado do groupby não está vazio antes de plotar
        if not vendas_por_cafe.empty:
            fig, ax = plt.subplots(figsize=(5, 2.2))
            vendas_por_cafe.plot(kind="bar", ax=ax)
            ax.set_xlabel("Produto", fontsize=8)
            ax.set_ylabel("Total (R$)", fontsize=8)
            ax.set_title("Total por tipo de café", fontsize=9)
            ax.tick_params(axis="y", labelsize=7)
            ax.tick_params(axis="x", labelsize=5)  # Fonte menor para os nomes dos produtos
            fig.tight_layout()
            st.pyplot(fig, clear_figure=True, use_container_width=True)
        else:
            st.info("Sem dados para o período selecionado.")
    else:
        st.info("Sem dados para o período selecionado.")

def grafico_dispersao(dff: pd.DataFrame):
    # Verifica se as colunas necessárias existem e se há dados
    if {"hora_do_dia", "valor"}.issubset(dff.columns) and not dff.empty:
        fig, ax = plt.subplots(figsize=(5, 2.2))
        # alpha controla a transparência e s o tamanho de cada ponto
        ax.scatter(dff["hora_do_dia"], dff["valor"], alpha=0.6, s=10)
        ax.set_xlabel("Hora do Dia", fontsize=8)
        ax.set_ylabel("Valor (R$)", fontsize=8)
        ax.set_title("Hora do dia x Valor da Venda", fontsize=9)
        ax.tick_params(axis="both", labelsize=7)
        fig.tight_layout()
        st.pyplot(fig, clear_figure=True, use_container_width=True)
    else:
        st.info("Sem dados para o período selecionado.")

def grafico_pizza(dff: pd.DataFrame):
    # Verifica se a coluna necessária existe e se há dados
    if "meio_de_pagamento" in dff.columns and not dff.empty:
        formas_pagamento = dff["meio_de_pagamento"].value_counts()  # Conta cada forma de pagamento
        fig, ax = plt.subplots(figsize=(5, 2.2))
        # autopct exibe o percentual em cada fatia; startangle=90 inicia o gráfico no topo
        ax.pie(formas_pagamento, labels=formas_pagamento.index, autopct="%1.1f%%", startangle=90, textprops={"fontsize": 8})
        ax.axis("equal")  # Garante que o gráfico seja um círculo perfeito
        ax.set_title("Formas de Pagamento", fontsize=9)
        fig.tight_layout()
        st.pyplot(fig, clear_figure=True, use_container_width=True)
    else:
        st.info("Sem dados para o período selecionado.")
