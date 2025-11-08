import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("Dashboard de Análisis de Explicaciones Estudiantiles")

tab1, tab2 = st.tabs(["Prueba de modelos realizados", "Dashboard Interactivo"])

with tab1:
    st.markdown("""
    Aquí va el dato que va al modelo para predecir
    """)

with tab2:
    powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=fce866ce-b39f-448f-a290-d1b294affaa5&autoAuth=true&ctid=73c3e337-a317-4624-bb03-047663c4d9ed"
    st.markdown("### Dashboard Interactivo")
    components.iframe(powerbi_url, height=800, scrolling=True)
