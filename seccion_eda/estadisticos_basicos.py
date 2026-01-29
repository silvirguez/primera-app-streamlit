import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown("")

df = pd.read_csv("bike_dataset_hour.csv")

st.markdown("## Datos Crudos del dataset")

st.dataframe(df.head(500))

st.markdown("## Datos sobre el dataset")

st.dataframe(df.describe().T)

st.markdown("## Estadisticos básicos")

st.dataframe(df[['dteday','temp','windspeed','cnt']].describe().T[['count','std','mean']])

st.markdown("## Distribución de las variables")

cols = st.columns(3)

with cols[0]:
    fig, ax = plt.subplots()
    sns.histplot(df['temp'], kde=True)
    plt.title('Distribucion Temp.')
    st.pyplot(fig)

with cols[1]:
    fig, ax = plt.subplots()
    sns.histplot(df['temp'], kde=True)
    plt.title('Distribucion Humedad')
    st.pyplot(fig)

with cols[2]:
    fig, ax = plt.subplots()
    sns.histplot(df['windspeed'], kde=True)
    plt.title('Distribucion velocidad del viento')
    st.pyplot(fig)

st.markdown("---")

cols_target, = st.columns(1)

with cols_target:
    fig, ax = plt.subplots()
    sns.histplot(df['cnt'], kde=True)
    plt.title('Distribucion de ventas')
    st.pyplot(fig)

st.markdown("## Matriz de correlación")

cols_interes = ['temp','hum','windspeed','casual','cnt']
matriz_correlacion = df[cols_interes].corr()

col, = st.columns(1)

with col:
    fig, ax= plt.subplots()
    sns.heatmap(matriz_correlacion, annot= True)
    plt.title("Matriz correlacion con cnt")
    st.pyplot(fig)
