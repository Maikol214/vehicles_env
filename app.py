import streamlit as st
import pandas as pd
import plotly.express as px

# Título del tablero
st.header('Análisis de Anuncios de Vehículos en EE.UU.')

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

st.write('Explora el conjunto de datos de anuncios de venta de vehículos en EE.UU.')
st.write('Selecciona una opción para visualizar los datos:')

# Crear una casilla de verificación para construir un histograma
build_hist = st.checkbox('Construir histograma del odómetro')

if build_hist:
    st.write('Histograma del kilometraje (odómetro)')
    fig_hist = px.histogram(car_data, x='odometer', nbins=30, title='Distribución del Odómetro')
    st.plotly_chart(fig_hist, use_container_width=True)

# Crear una casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión (precio vs kilometraje)')

if build_scatter:
    st.write('Relación entre el precio y el kilometraje del vehículo')
    fig_scatter = px.scatter(car_data, x='odometer', y='price',
                             title='Precio vs Odómetro',
                             color='type',  # si existe la columna 'type'
                             hover_data=['model', 'model_year'])
    st.plotly_chart(fig_scatter, use_container_width=True)
