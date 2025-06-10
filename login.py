def handle_device_flow():
    device_flow = st.session_state.get("device_flow")
    if not device_flow:
        st.error("Sessione di device flow non trovata. Riprova.")
        st.stop()

    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET
    )
    # Prova a prendere il token
    result = msal_app.acquire_token_by_device_flow(device_flow)

    # 🔍 Debug extra: mostra il risultato completo
    st.write("🔄 Result from acquire_token_by_device_flow():", result)

    # 🔍 Debug extra: mostra session state dopo tentativo
    st.write("📦 Session state subito dopo polling:", dict(st.session_state))

    if result and "access_token" in result:
        st.session_state["authenticated"] = True
        st.session_state["token"] = result
        st.experimental_rerun()
    else:
        err  = result.get("error", "unknown_error")
        desc = result.get("error_description", "")
        st.error(f"❌ Errore token: {err} — {desc}")
        st.stop()
