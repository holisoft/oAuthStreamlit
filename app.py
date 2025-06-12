# app.py
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher

# ------------------------------------------------------------
# 1) Definisci le credenziali in chiaro
# ------------------------------------------------------------
raw_credentials = {
    "usernames": {
        "admin": {
            "name": "Amministratore",
            "password": "password"   # password in chiaro
        }
        # → aggiungi qui altri utenti, sempre con chiave "username"
    }
}

# ------------------------------------------------------------
# 2) Genera gli hash per tutte le password
# ------------------------------------------------------------
credentials = Hasher.hash_passwords(raw_credentials)  # classmethod che sostituisce .generate() :contentReference[oaicite:0]{index=0}

# ------------------------------------------------------------
# 3) Parametri cookie (cambia cookie_key in produzione!)
# ------------------------------------------------------------
cookie_name        = "holisoft_auth"
cookie_key         = "STRINGA_SEGRETA_E_RANDOMICA_DI_ALMENO_32_CARATTERI"
cookie_expiry_days = 30
preauthorized      = []  # lista di email se ne hai

# ------------------------------------------------------------
# 4) Crea l’istanza dell’Authenticator
# ------------------------------------------------------------
authenticator = stauth.Authenticate(
    credentials,
    cookie_name,
    cookie_key,
    cookie_expiry_days,
    preauthorized,
    auto_hash=False       # già abbiamo hashato noi le password
)

# ------------------------------------------------------------
# 5) Mostra il form di login (location="main") 
# ------------------------------------------------------------
authenticator.login(location="main")  # popola st.session_state :contentReference[oaicite:1]{index=1}

# ------------------------------------------------------------
# 6) Leggi lo stato da session_state
# ------------------------------------------------------------
auth_status = st.session_state.get("authentication_status")
user_name   = st.session_state.get("name")

if auth_status:
    # login OK
    st.sidebar.success(f"✅ Benvenuto, {user_name}!")
    st.title("🚀 Dashboard riservata")
    st.write("Qui puoi mettere i contenuti per utenti autenticati.")
    authenticator.logout(location="sidebar")

elif auth_status is False:
    # credenziali errate
    st.error("❌ Username o password errati")

else:
    # ancora non hai cliccato “Login”
    st.info("🔒 Inserisci username e password")
