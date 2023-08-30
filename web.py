import streamlit as st
import pandas as pn
st.set_page_config(layout='wide')

col1, col2 = st.columns(2)
with col1:
    st.image("images/naveed.jpg", caption='NaveedZaynali')

with col2:
    st.title("my resume as a python developer")
    st.info('''
    born in Tehran \n date of birth 1999.01.17\n
    son of Naser \n I'll be happy to show you some of my apps build with python
    ''')

st.write('below you can find some of the apps i have built in python . feel free to contact me!')

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pn.read_csv("data/data.csv", sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.image("images/"+row['image'])
        st.write(f"[source]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.image("images/"+row['image'])
        st.write(f"[source]({row['url']})")
