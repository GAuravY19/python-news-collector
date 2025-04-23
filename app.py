import streamlit as st
import os
from main import MainRun
from names import NAMES

st.header('News Scrapper')

col1, col2, col3 = st.columns(3)

with col1:
    st.image(os.path.join(os.getcwd(), "static", 'google.png'), caption='Scrape Google News', width=150)
    google_select = st.button('Select', key='Google')

with col2:
    st.image(os.path.join(os.getcwd(), "static", 'linkedin.png'), caption='Scrape Linkedin', width=150)
    linkedin_select = st.button('Select', key='Linkedin')

with col3:
    st.image(os.path.join(os.getcwd(), "static", 'twitter.png'), caption='Scrape Twitter', width=150)
    twitter_select = st.button('Select', key='Twitter')


if google_select:
    st.subheader('Google News Selected')
    MainRun()

elif linkedin_select:
    st.subheader('Linkedin Selected')
    st.markdown("Coming Soon")

elif twitter_select:
    st.subheader('Twitter Selected')
    st.markdown("Coming Soon")


