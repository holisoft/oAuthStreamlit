# app.py
import streamlit as st
import streamlit_authenticator as stauth

# ------------------------------------------------------------
# 1) Configurazione delle credenziali
# ------------------------------------------------------------
credentials = {
    "usernames": {
        "admin": {
            "name": "Amministratore",
            # hash bcrypt di "password"
            "password": "$2b$12$KIXQG1fE/NAiPdMDH3pU3eI5/Ju9i9KHx3aLmYtUCRsLjaxHXSZX2"
        }
        # puoi aggiungere altri utenti qui...
    }
}

# ------------------------------------------------------------
# 2) Parametri cookie
# ------------------------------------------------------------
cookie_name = "holisoft_auth"
cookie_key = "ciccio"  # 🔐
cookie_expiry_days = 30
preauthorized = []  # email pre-autorizzate, se ne hai

# Istanza dell’autenticatore
authenticator = stauth.Authenticate(
    credentials,
    cookie_name,
    cookie_key,
    cookie_expiry_days,
    preauthorized
)

# ------------------------------------------------------------
# 3) Login widget (ritorna sempre None se location ≠ 'unrendered')
# ------------------------------------------------------------
authenticator.login(location="main")  # rende il form e popola st.session_state :contentReference[oaicite:1]{index=1}

# ------------------------------------------------------------
# 4) Gestione dello stato di autenticazione
# ------------------------------------------------------------
auth_status = st.session_state.get("authentication_status")

if auth_status:
    # utente autenticato
    name = st.session_state.get("name")
    st.sidebar.success(f"✅ Benvenuto, {name}!")
    
    # — CONTENUTO DELL’APP per utenti loggati —
    st.title("Dashboard riservata")
    st.write("Ecco i contenuti a cui hai accesso solo tu.")
    # ---------------------------------------------

    # pulsante di logout in sidebar
    authenticator.logout(location="sidebar")

elif auth_status is False:
    # credenziali errate
    st.error("❌ Username o password errati")

else:
    # auth_status è None: nessun tentativo di login ancora fatto
    st.info("🔒 Inserisci username e password")
