import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

# Menú lateral
opcion = st.sidebar.radio(
    "Selecciona una actividad",
    ("Actividad 1", "Actividad 2", "Actividad 3")
)

# Actividad 1
if opcion == "Actividad 1":
    st.title("Actividad 5.3 (1)")
    st.write('Hello world!')
    st.write("Mario Alberto González Méndez")
    st.write("Esta es mi primera página web con Streamlit")
    st.write("El día de hoy comí una hamburguesa con doble carne")
    st.write("También aprendí acerca de los entornos para configurar Streamlit")
    st.write("Y por último, aprendí a crear una página web con Streamlit")
    st.write("¡Espero que les guste mi página web!")

# Actividad 2
elif opcion == "Actividad 2":
    st.title("Actividad 5.3 (2)")
    st.header('Adivina dónde está Superman')

    if st.button('Opción 1 - en el cielo'):
        st.write('❌ No, Superman no está en el cielo.')

    if st.button('Opción 2 - en la tierra'):
        st.write('❌ No, Superman no está en la tierra.')

    if st.button('Opción 3 - en la luna'):
        st.write('✔️ Correcto, Superman está ahorita en la luna.')

# Actividad 3
elif opcion == "Actividad 3":
    st.title("Actividad 5.3 (3)")
    st.header('st.write')

    st.write('Hello, *World!* :sunglasses:')
    st.write(1234)


    st.header("Datos del Titanic y Diabetes")

    st.subheader("Datos del Titanic")
    df = pd.read_csv("titanic.csv")
    st.write(df)

    st.subheader("Datos de Diabetes")
    df2 = pd.read_csv("diabetes.csv")
    st.write(df2)


    st.subheader("Gráfico de Diabetes")
    
    c = alt.Chart(df2).mark_circle().encode(
        x='Pregnancies', y='Glucose', size='Insulin', color='BMI', tooltip=['Pregnancies', 'Glucose', 'Insulin', 'BMI']
    )
    st.write(c)
