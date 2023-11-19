import streamlit as st
import pandas as pd
import numpy as np

from config.configvars import *

st.title('Uber pickups in NYC')




# Load environment variables from the .env file
import MySQLdb

print(DATABASE_HOST, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE)

# Connect to the database
connection = MySQLdb.connect(
  host= DATABASE_HOST,
  user= DATABASE_USERNAME,
  passwd= DATABASE_PASSWORD,
  db= DATABASE,
  autocommit=True,
  ssl_mode="VERIFY_IDENTITY",
  # See https://planetscale.com/docs/concepts/secure-connections#ca-root-configuration
  # to determine the path to your operating systems certificate file.
  ssl={ "ca": "/etc/ssl/certs/ca-certificates.crt" }
)


