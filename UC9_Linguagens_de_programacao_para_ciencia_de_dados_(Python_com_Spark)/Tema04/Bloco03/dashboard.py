#*************************************
# PARA EXECUTAR O ARQUIVO, execute o comando abaixo no terminal:
# streamlit run TeoriaEmPratica.py
#*************************************

import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")
st.title("Dashboard Interativo - Exemplo")

# Criação de dados de exemplo
np.random.seed(42)
df = pd.DataFrame({
    'Data': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'Vendas': np.random.randint(100, 1000, 365),
    'Categoria': np.random.choice(['A', 'B', 'C'], 365),
    'Região': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], 365)
})

print(df.head())

# Sidebar para filtros
st.sidebar.title("Filtros")
categoria = st.sidebar.multiselect("Selecione a categoria", options=df['Categoria'].unique(), default=df['Categoria'].unique())
regiao = st.sidebar.multiselect("Selecione a região", options=df['Região'].unique(), default=df['Região'].unique())

# Filtragem dos dados
df_filtrado = df[(df['Categoria'].isin(categoria)) & (df['Região'].isin(regiao))]

# Layout em duas colunas
# col1, col2 = st.columns(2)
col1, col2 = st.columns([1, 2])

# Gráfico de barras
with col1:
    st.subheader("Vendas por categoria")
    fig_barras = px.bar(df_filtrado.groupby('Categoria')['Vendas'].sum().reset_index(), x='Categoria', y='Vendas', color='Categoria')
    st.plotly_chart(fig_barras)

# Gráfico de dispersão
with col2:
    st.subheader("Vendas por região")
    fig_dispersao = px.scatter(df_filtrado, x='Data', y='Vendas', color='Região')
    st.plotly_chart(fig_dispersao, use_container_width=True)

# Métricas
st.subheader("Métricas")
col1, col2, col3 = st.columns(3)
col1.metric("Total de vendas", f"R$ {df_filtrado['Vendas'].sum():,.2f}")
col2.metric("Média de Vendas Diárias", f"R$ {df_filtrado['Vendas'].mean():,.2f}")
col3.metric("Número de Dias", df_filtrado['Data'].nunique())

# Tabela de dados
st.subheader("Tabela de Dados")
st.dataframe(df_filtrado)

# Nota sobre interatividade
st.info("Para interagir com o dashboard, utilize os filtros na barra lateral.")
