import streamlit as st
import pandas as pd
import numpy as np
from utils.dbmanager import DBConnection
# from utils.configvars import views, devices
from view import views_dict

st.title('Terrarium DashBoard')


dbconn = DBConnection()
view = st.selectbox("Select view", views_dict.keys() , index= 1)

def get_devices(device_type:str):
  query = f"SELECT * FROM data_{device_type.lower()}"
  df = dbconn.execute_read_query(query)
  return df


if view is not None:
  views_dict[view](dbconn)

