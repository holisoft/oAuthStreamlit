import streamlit as st
import streamlit_authenticator as stauth
from dotenv import load_dotenv

load_dotenv()

# Carica credenziali dal secrets.toml
credentials = st.secrets["credentials"]

authenticator = stauth.Authenticate(
    credentials,
    cookie_name="holisoft_auth",
    key="some-random-signature-key",  # cambia con una stringa a caso
    cookie_expiry_days=1
)

# Schermata di login
name, authentication_status, username = authenticator.login("Login", "main")

if not authentication_status:
    if authentication_status is False:
        st.error("❌ Username o password errati")
    st.stop()

# Se siamo qui, siamo autenticati
st.success(f"✅ Benvenuto, {name}!")

# Il pulsante di logout
authenticator.logout("Logout", "main")

# ———— Qui inizia la tua app protetta ————
st.markdown("---")
st.write("🚀 Contenuto riservato alla tua app!")
