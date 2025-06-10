# login.py
import streamlit as st
import os
import msal
import secrets
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID     = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
TENANT_ID     = os.getenv("AZURE_TENANT_ID")
REDIRECT_URI  = os.getenv("AZURE_REDIRECT_URI")
AUTHORITY     = f"https://login.microsoftonline.com/{TENANT_ID}"

# Chiediamo sia un id_token (openid+profile) sia un access_token per Graph
SCOPES = ["openid", "profile", "User.Read"]

def show():
    st.title("🔐 Login con Azure AD")

    # Crea app MSAL
    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )

    # Genera uno state casuale e salvalo in session_state
    state = secrets.token_urlsafe(16)
    st.session_state["oauth_state"] = state

    # URL di autorizzazione
    auth_url = msal_app.get_authorization_request_url(
        SCOPES,
        state=state,
        redirect_uri=REDIRECT_URI,
        prompt="select_account"
    )
    st.markdown(f"[➡️ Accedi con il tuo account Microsoft]({auth_url})")

def handle_callback():
    params = st.query_params
    code  = params.get("code", [None])[0]
    state = params.get("state", [None])[0]

    # Debug chiave
    st.write("🔍 code ricevuto:", code)
    st.write("🔍 state ricevuto:", state)
    st.write("🔍 state atteso:", st.session_state.get("oauth_state"))

    # Verifica che il state combaci
    if not code or state != st.session_state.get("oauth_state"):
        st.error("❌ Stato non valido o assente. Riprova da capo.")
        st.stop()

    # Richiedi il token
    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )
    result = msal_app.acquire_token_by_authorization_code(
        code,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )

    # Mostra il risultato grezzo per capire eventuali errori
    st.write("⚙️ Risultato MSAL:", result)

    if "access_token" in result:
        st.session_state["authenticated"] = True
        st.session_state["token"] = result
        st.experimental_rerun()
    else:
        err = result.get("error", "unknown_error")
        desc = result.get("error_description", "")
        st.error(f"❌ Errore durante fetch token: {err} — {desc}")
        st.stop()
