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
# In alcune versioni di streamlit-authenticator l'ordine dei parametri
# della funzione login è (location, form_name). Utilizziamo quindi
# prima la posizione e poi il nome del form.
name, authentication_status, username = authenticator.login(
    "main",
    "Login"
)

# Gestione stato autenticazione
if authentication_status:
    st.success(f"✅ Login effettuato con successo! Benvenuto, {name}.")
elif authentication_status is False:
    st.error("❌ Login fallito. Controlla credenziali.")
else:
    st.info("🔒 Inserisci username e password.")
