import streamlit as st
import pandas as pd

# st.set_page_config(layout = "wide")

st.set_page_config()
col1, col2 = st.columns(2)

with col1:
    st.image("images/damgom.jpg")

with col2:
    st.title("Nagano Bear")
    content = """
    Hello, I am Damgom. I am a bear, but very cool and handsome."""
    st.info(content)

content2 = """
Below you can fid some of the apps I have built in Python. Feel free to contact me!"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv('data.csv', sep = ';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/"+ row['image'])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/"+ row['image'])
        st.write(f"[Source Code]({row['url']})")