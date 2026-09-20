import pandas as pd
import plotly.express as px
import streamlit as st

# Título da aplicação Web
st.header("Análise de Anúncios de Veículos")

# Carrega o conjunto de dados
car_data = pd.read_csv('vehicles.csv')

# Botão para gerar o Histograma
hist_button = st.button('Criar histograma')

if hist_button:  # se o botão for clicado
    # Escreve uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros'
    )

    # Cria um histograma
    fig = px.histogram(car_data, x="odometer")

    # Exibe um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

    # Botão para gerar o Gráfico de Dispersão (Scatter Plot)
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:  # se o botão for clicado
    # Escreve uma mensagem
    st.write(
        'Criando um gráfico de dispersão para preço vs. quilometragem'
    )

    # Cria um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")

    # Exibe um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)