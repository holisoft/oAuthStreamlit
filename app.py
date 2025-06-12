import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher

# ------------------------------------------------------------
# 1) Lettura delle credenziali e del cookie_key da secrets
# ------------------------------------------------------------
raw_credentials = {"usernames": {}}
# streamlit.secrets["credentials"]["usernames"] è un dict di dicts:
for username, data in st.secrets["credentials"]["usernames"].items():
    raw_credentials["usernames"][username] = {
        "name": data["name"],
        "password": data["password"]  # password in chiaro
    }

cookie_name        = "holisoft_auth"
cookie_key         = st.secrets["cookie_key"]
cookie_expiry_days = 30
preauthorized      = []

# ------------------------------------------------------------
# 2) Hashing delle password in runtime (bcrypt compatibile)
# ------------------------------------------------------------
# Hasher.hash_passwords trasforma raw_credentials in dict con password hashed
credentials = Hasher.hash_passwords(raw_credentials)

# ------------------------------------------------------------
# 3) Creazione dell'autenticatore
# ------------------------------------------------------------
authenticator = stauth.Authenticate(
    credentials,
    cookie_name,
    cookie_key,
    cookie_expiry_days,
    preauthorized,
    auto_hash=False  # già abbiamo effettuato l'hash
)

# ------------------------------------------------------------
# 4) Mostra il form di login (popola st.session_state)
# ------------------------------------------------------------
authenticator.login(location="main")

# ------------------------------------------------------------
# 5) Leggi lo stato di autenticazione
# ------------------------------------------------------------
auth_status = st.session_state.get("authentication_status")
user_name   = st.session_state.get("name")

if auth_status:
    st.sidebar.success(f"✅ Benvenuto, {user_name}!")
    st.title("🚀 Dashboard riservata")
    st.write("Contenuto protetto per utenti autenticati.")
    authenticator.logout(location="sidebar")

elif auth_status is False:
    st.error("❌ Username o password errati")

else:
    st.info("🔒 Inserisci username e password")