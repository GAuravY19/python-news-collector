from click import option
import streamlit as st
import os
from googlescrapper import MainRun
from gurls.names import NAMES
from youtube import main_youtube

st.header('News Scrapper')

col1, col2 = st.columns(2)

with col1:
    st.image(os.path.join(os.getcwd(), "static", 'google.png'), caption='Scrape Google News', width=150)
    google_select = st.button('Select', key='Google')

with col2:
    st.image(os.path.join(os.getcwd(), "static", 'youtube.png'), caption='Scrape Youtube', width=150)
    Youtube_select = st.button('Select', key='Youtube')

if google_select:
    st.subheader('Google News Selected')

    MainRun()



elif Youtube_select:
    st.subheader('Youtube Selected')
    main_youtube()


