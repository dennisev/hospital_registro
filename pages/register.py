# pages\register.py
import streamlit as st
import pandas as pd
import os

def show_register_page(user_role):
    st.title("Registrar Paciente")

    # Crear columnas para posicionar el botón en la derecha
    header_cols = st.columns([8, 1])
    with header_cols[1]:
        if st.button("Cerrar Sesión"):
            st.session_state.authenticated = False
            st.session_state.user_role = None
            st.session_state.page = 'Registrar Paciente'
            st.rerun()

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("images/logo.png", use_column_width=True)
        st.image("images/surgery.png", use_column_width=True)

    with col2:
        nombre = st.text_input("Nombre")
        edad = st.number_input("Edad", min_value=0)
        genero = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])
        diagnostico = st.text_area("Diagnóstico")

        # Crear una fila para los botones
        button_cols = st.columns(2)
        with button_cols[0]:
            if st.button("Registrar"):
                new_patient = {
                    'Nombre': nombre,
                    'Edad': edad,
                    'Género': genero,
                    'Diagnóstico': diagnostico
                }
                save_patient(new_patient)
                st.success("Paciente registrado exitosamente")

        if user_role == 'admin':
            with button_cols[1]:
                if st.button("Ver Tabla de Pacientes"):
                    st.session_state.page = 'Ver Tabla'
                    st.rerun()

def save_patient(patient_data):
    file_path = "data/patients.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=['Nombre', 'Edad', 'Género', 'Diagnóstico'])

    # Crear un DataFrame a partir de los datos del paciente
    new_patient_df = pd.DataFrame([patient_data])

    # Usar pd.concat para agregar la nueva fila
    df = pd.concat([df, new_patient_df], ignore_index=True)

    df.to_csv(file_path, index=False)