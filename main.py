import streamlit as st

st.set_page_config(layout = "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/profile.png")

with col2:
    st.title("SH Cha")
    content = """
    Hello, I am BeeBean23. I am a Data Analyst, AI Image designer and game blogger."""
    st.info(content)