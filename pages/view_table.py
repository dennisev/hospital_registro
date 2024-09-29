# pages/view_table.py
import streamlit as st
import pandas as pd

def show_table_page():
    st.title("Tabla de Pacientes")

    # Botón para volver a la página de registro
    if st.button("Registrar Paciente"):
        st.session_state.page = 'Registrar Paciente'
        st.rerun()

    df = pd.read_csv("data/patients.csv")

    # Filtros
    nombre_filter = st.text_input("Filtrar por Nombre")
    genero_filter = st.multiselect("Filtrar por Género", options=df['Género'].unique())

    if nombre_filter:
        df = df[df['Nombre'].str.contains(nombre_filter, case=False)]

    if genero_filter:
        df = df[df['Género'].isin(genero_filter)]

    st.dataframe(df)
