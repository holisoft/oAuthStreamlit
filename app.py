# app.py
import streamlit as st
import streamlit_authenticator as stauth

# ------------------------------------------------------------
# 1) Configurazione delle credenziali (come nel tuo esempio)
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
# 2) Parametri cookie (sostituisci key con un segreto tuo)
# ------------------------------------------------------------
cookie_name = "holisoft_auth"
cookie_key = "SOSTITUISCI_CON_UNA_STRINGA_CASUALE_E_SEGRETA"  # 🔐
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
# 3) Login: restituisce (name, authentication_status, username)
# ------------------------------------------------------------
name, authentication_status, username = authenticator.login("main")  # location = 'main' :contentReference[oaicite:0]{index=0}

# ------------------------------------------------------------
# 4) Gestione dello stato di autenticazione
# ------------------------------------------------------------
if authentication_status:
    # utente autenticato
    st.sidebar.success(f"✅ Benvenuto, {name}!")
    
    # — CONTENUTO DELL’APP per utenti loggati —
    st.title("Dashboard riservata")
    st.write("Ecco i contenuti a cui hai accesso solo tu.")
    # ---------------------------------------------

    # pulsante di logout in sidebar
    authenticator.logout("sidebar")

elif authentication_status is False:
    # credenziali errate
    st.error("❌ Username o password errati")

else:
    # stato None = nessun tentativo di login ancora fatto
    st.info("🔒 Inserisci username e password")
