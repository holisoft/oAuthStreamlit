import streamlit as st
import os
import msal
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID     = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
TENANT_ID     = os.getenv("AZURE_TENANT_ID")
REDIRECT_URI  = os.getenv("AZURE_REDIRECT_URI")
AUTHORITY     = f"https://login.microsoftonline.com/{TENANT_ID}"

# Scope Graph API
SCOPES = ["User.Read"]

def show():
    st.title("🔐 Login con Azure AD")
    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )
    auth_url = msal_app.get_authorization_request_url(
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,
        prompt="select_account"
    )
    st.markdown(f"[➡️ Accedi con il tuo account Microsoft]({auth_url})")

def handle_callback():
    params = st.query_params
    code = params.get("code", [None])[0]

    if not code:
        st.error("❌ Nessun codice di autorizzazione ricevuto. Riprova da capo.")
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

    # Debug: mostra l’intero risultato
    st.write("⚙️ Risultato MSAL:", result)

    if "access_token" in result:
        st.session_state["authenticated"] = True
        st.session_state["token"] = result
        st.experimental_rerun()
    else:
        err  = result.get("error", "unknown_error")
        desc = result.get("error_description", "")
        st.error(f"❌ Errore fetch token: {err} — {desc}")
        st.stop()
