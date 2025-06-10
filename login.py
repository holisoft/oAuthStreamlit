# login.py
import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
TENANT_ID = os.getenv("AZURE_TENANT_ID")
REDIRECT_URI = os.getenv("AZURE_REDIRECT_URI")

AUTH_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize"
TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
SCOPE = ["openid", "profile", "email"]

def show():
    st.title("Login con Azure")

    if "token" not in st.session_state:
        oauth = OAuth2Session(CLIENT_ID, CLIENT_SECRET, scope=SCOPE, redirect_uri=REDIRECT_URI)
        authorization_url, state = oauth.create_authorization_url(AUTH_URL)
        st.session_state["oauth_state"] = state
        st.markdown(f"[Clicca qui per accedere con il tuo account Microsoft]({authorization_url})")
        st.stop()
    else:
        st.success("Accesso effettuato con successo.")

def handle_callback():
    from urllib.parse import parse_qs, urlparse

    query_params = st.query_params
    if "code" in query_params:
        code = query_params["code"]
        oauth = OAuth2Session(CLIENT_ID, CLIENT_SECRET, scope=SCOPE, redirect_uri=REDIRECT_URI)
        token = oauth.fetch_token(TOKEN_URL, code=code, grant_type='authorization_code')
        st.session_state["token"] = token
