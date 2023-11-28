import streamlit as st
import pandas as pd
from utils.dbmanager import DBConnection

def view(dbconn: DBConnection):
    query = "SELECT * FROM data_dht11"
    df = dbconn.execute_read_query(query)
    st.write(df)