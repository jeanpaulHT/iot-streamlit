import streamlit as st

DATABASE_HOST=st.secrets["DATABASE_HOST"] 
DATABASE_USERNAME=st.secrets["DATABASE_USERNAME"]
DATABASE_PASSWORD=st.secrets["DATABASE_PASSWORD"]
DATABASE=st.secrets["DATABASE"]


devices = ["DHT11"]
views = ["DHT11", "Rules"]
