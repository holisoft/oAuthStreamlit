# login.py
import streamlit as st
import os
from dotenv import load_dotenv
import msal

load_dotenv()

CLIENT_ID     = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
TENANT_ID     = os.getenv("AZURE_TENANT_ID")
REDIRECT_URI  = os.getenv("AZURE_REDIRECT_URI")
AUTHORITY     = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES        = ["User.Read"]  # o altri scope a tua scelta

def show():
    st.title("🔐 Login con Azure AD")
    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )
    auth_url = msal_app.get_authorization_request_url(
        SCOPES,
        redirect_uri=REDIRECT_URI,
        state="abcdef",  # puoi generare uno state casuale se vuoi
    )
    st.markdown(f"[Clicca qui per accedere con Microsoft]({auth_url})")

def handle_callback():
    params = st.query_params
    code = params.get("code", [None])[0]

    if not code:
        st.error("❌ Nessun codice di autorizzazione ricevuto.")
        st.stop()

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

    if "access_token" in result:
        st.session_state["authenticated"] = True
        st.session_state["token"] = result
        st.experimental_rerun()
    else:
        st.error("❌ Errore durante il fetch del token:")
        st.write(result.get("error_description"))
        st.stop()
