# app.py
# Esempio di semplice autenticazione in Streamlit usando streamlit-authenticator
# Dipendenze (requirements.txt):
# streamlit
# streamlit-authenticator
# python-dotenv    (opzionale, se vuoi usare .env)

import streamlit as st
import streamlit_authenticator as stauth

# Configura le credenziali direttamente nel codice per semplicità
# In produzione, sposta questi valori nei secrets di Streamlit o in un file .env
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
    cookie_name="streamlit_auth",  # nome del cookie
    key="12345",                   # chiave di firma qualsiasi
    cookie_expiry_days=1            # durata del cookie
)

st.title("Esempio di Login Streamlit")

# Mostra la form di login
name, authentication_status, username = name, authentication_status, username = authenticator.login("Login", location="main")
    "Login",
    "main"
)

# Gestione stato autenticazione
if authentication_status:
    st.success(f"✅ Login effettuato con successo! Benvenuto, {name}.")
elif authentication_status is False:
    st.error("❌ Login fallito. Controlla credenziali.")
else:
    st.info("🔒 Inserisci username e password.")

# In produzione puoi mostrare un pulsante di logout:
# authenticator.logout("Logout", "main")
