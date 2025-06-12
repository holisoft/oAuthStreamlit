# app.py
# Esempio di semplice autenticazione in Streamlit usando streamlit-authenticator
# Dipendenze (requirements.txt):
# streamlit
# streamlit-authenticator

import streamlit as st
import streamlit_authenticator as stauth

# Configura le credenziali direttamente nel codice per semplicità
credentials = {
    "usernames": {
        "admin": {
            "name": "Amministratore",
            # hash bcrypt di "password"
            "password": "$2b$12$KIXQG1fE/NAiPdMDH3pU3eI5/Ju9i9KHx3aLmYtUCRsLjaxHXSZX2"
        }
    }
}

# Inizializza l'autenticatore
authenticator = stauth.Authenticate(
    credentials,
    cookie_name="streamlit_auth",
    key="12345",
    cookie_expiry_days=1
)

st.title("Esempio di Login Streamlit")

# Mostra la form di login
# decompattazione a 2 variabili (non più 3)
authentication_status, username = authenticator.login(
    "Login",
    "main"
)

# Gestione stato autenticazione
if authentication_status:
# prendi il nome “umano” dal dict delle credenziali
    name = credentials["usernames"][username]["name"]
    st.success(f"✅ Benvenuto, {name}!")
elif authentication_status is False:
    st.error("❌ Login fallito")
else:
    st.info("🔒 Inserisci username e password")

