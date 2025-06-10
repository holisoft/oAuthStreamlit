import streamlit as st
import login

st.set_page_config(page_title="Login", layout="wide")

# Gestione login
if "authenticated" not in st.session_state:
    if "code" in st.query_params:
        login.handle_callback()
    else:
        login.show()
    st.stop()

# Contenuto se autenticato
st.success("Login effettuato con successo!")
st.write("Contenuto della dashboard...")
