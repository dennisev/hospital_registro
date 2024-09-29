# pages\login.py
import streamlit as st
from src.authentication import authenticate_user

def show_login_page():
    st.title("Login")

    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        user = authenticate_user(username, password)
        if user:
            st.session_state.authenticated = True
            st.session_state.user_role = 'admin' if user == 'admin' else 'user'
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos")
