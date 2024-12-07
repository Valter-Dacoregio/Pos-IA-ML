#*************************************
# PARA EXECUTAR O ARQUIVO, execute o comando abaixo no terminal:
# streamlit run TeoriaEmPratica.py
#*************************************

import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Configuração da página
st.set_page_config(page_title="Painel de Vendas - Varejo On-line S.A.", page_icon=":bar_chart:", layout="wide")

# Função para gerar dados de exemplo
@st.cache_data
def gerar_dados():
    df_vendas = pd.DataFrame({
        'Data': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
        'Vendas': np.random.randint(1000, 5000, 365),
        'Categoria': np.random.choice(['Eletrônicos', 'Roupas', 'Livros', 'Casa', 'Esportes'], 365),
    })

    df_clientes = pd.DataFrame({
        'Data': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
        'Novos_Clientes': np.random.randint(10, 100, 365),
        'Satisfação': np.random.randint(1, 5, 365),
    })

    df_produtos = pd.DataFrame({
        'Produto': ['Smartphone', 'Notebook', 'Tênis', 'Livro', 'Camiseta'],
        'Vendas': [1500, 12000, 9000, 7500, 6000],
        'Avaliação': [4.5, 4.8, 4.3, 4.7, 4.2],
        'Categoria': ['Eletrônicos', 'Eletrônicos', 'Esportes', 'Livros', 'Roupas']
    })

    return df_vendas, df_clientes, df_produtos

# Carregamento dos dados
df_vendas, df_clientes, df_produtos = gerar_dados()


# Sidebar com filtros
st.sidebar.title("Filtros")
categoria_selecionada = st.sidebar.multiselect(
    "Selecione a categoria", 
    options=df_vendas['Categoria'].unique(), 
    default=df_vendas['Categoria'].unique()
)

# Filtragem dos dados
df_vendas_filtrado = df_vendas[df_vendas['Categoria'].isin(categoria_selecionada)]
df_produtos_filtrado = df_produtos[df_produtos['Categoria'].isin(categoria_selecionada)]

# Título do painel
st.title("Painel de Vendas - Varejo On-line S.A.")

# Métricas principais
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Vendas", f"R$ {df_vendas_filtrado['Vendas'].sum():,.2f}")
with col2:
    st.metric("Novos Clientes", df_clientes['Novos_Clientes'].sum())
with col3:
    st.metric("Satisfação Média", f"{df_clientes['Satisfação'].mean():.2f}")



# Gráfico de vendas ao longo do tempo
st.subheader("Vendas ao longo do tempo")
fig_vendas_tempo = px.line(df_vendas_filtrado, x='Data', y='Vendas', color='Categoria')
st.plotly_chart(fig_vendas_tempo)

# Gráfico de vendas por categoria
st.subheader("Vendas por categoria")
df_cat = df_vendas_filtrado.groupby('Categoria')['Vendas'].sum().reset_index()
fig_vendas_categoria = px.pie(df_cat, values='Vendas', names='Categoria', title='Título')
st.plotly_chart(fig_vendas_categoria)

# Gráficos de novos clientes e satisfação
col1, col2 = st.columns(2)

with col1:
    st.subheader("Novos Clientes por Dia")
    fig_novos_clientes = px.bar(df_clientes, x='Data', y='Novos_Clientes')
    st.plotly_chart(fig_novos_clientes, use_container_width=True)

with col2:
    st.subheader("Satisfação dos Clientes ao longo do Tempo")
    fig_satisfacao = px.line(df_clientes, x='Data', y='Satisfação')
    st.plotly_chart(fig_satisfacao, use_container_width=True)

# Gráfico de top produtos
st.subheader("Top Produtos: Vendas vs. Avaliação")
fig_top_produtos = px.scatter(df_produtos_filtrado, x='Vendas', y='Avaliação', size='Vendas', 
                              text='Produto', title='Top Produtos: Vendas vs. Avaliação', color='Categoria')
fig_top_produtos.update_traces(textposition='top center')
st.plotly_chart(fig_top_produtos, use_container_width=True)

# Tabela de dados
st.subheader("Dados Detalhados")
tab1, tab2, tab3 = st.tabs(["Vendas", "Clientes", "Produtos"])

with tab1:
    st.dataframe(df_vendas_filtrado)
with tab2:
    st.dataframe(df_clientes)
with tab3:
    st.dataframe(df_produtos_filtrado)


# Conclusão e Recomendações
st.markdown(f"""
## Conclusão e Recomendações

Com base nos dados apresentados, podemos concluir que:

1. As vendas têm tendência de crescimento ao longo do tempo, com destaque para a categoria de Eletrônicos.
2. A categoria mais vendida é {df_cat['Categoria'].iloc[0]}, representando {df_cat['Vendas'].iloc[0]/df_cat['Vendas'].sum():.2%} do total de vendas.
3. A aquisição de novos clientes e consistente, com uma média de {df_clientes['Novos_Clientes'].mean():.0f} novos clientes por dia.
4. A satisfação dos clientes mantém-se estável, com um média de {df_clientes['Satisfação'].mean():.2f} ao longo do tempo.
5. Os produtos mais vendidos são os {df_produtos_filtrado['Produto'].iloc[0]} e {df_produtos_filtrado['Produto'].iloc[1]}, ambos da categoria de Eletrônicos.

Recomendações:

- Focar em estratégias de marketing para as categorias menos vendidas, especialmente {df_cat['Categoria'].iloc[-1]}.
- Investigar as razões dos picos de aquisição de novos clientes nos dias {', '.join(df_clientes.nlargest(3, 'Novos_Clientes')['Data'].dt.strftime('%d/%m/%Y'))}.
- Implementar um programa de fidelidade para manter a satisfação dos clientes em alta, visando ultrapassar a média de {df_clientes['Satisfação'].mean():.2f}.
- Melhorar a qualidade dos produtos mais vendidos, mas com avaliações mais baixas, como a {df_produtos_filtrado['Produto'].iloc[-1]}.
- Considerar a expansão do estoque de produtos bem avaliados e com boas vendas, como o {df_produtos_filtrado['Produto'].iloc[1]}.
- Realizar uma análise mais profunda da sazonalidade das vendas para otimizar o estoque e as promoções.

""")