import streamlit as st
import pandas as pd
from utils.dbmanager import DBConnection

def get_sensor_devices(dbconn: DBConnection, sensor_type:str  ):
    table = "actuator" if sensor_type is None else f"data_{sensor_type.lower()}"
    query = f"SELECT * FROM {table}"
    df = dbconn.execute_read_query(query)
    return df

def get_rules(dbconn: DBConnection):
    query = "SELECT * FROM rules"
    df = dbconn.execute_read_query(query)
    return df


def get_actors(dbconn: DBConnection):
    query = "SELECT * FROM actuator"
    df = dbconn.execute_read_query(query)
    return df

@st.cache_data
def sensor_types():
    return ('dht11',)

def save_rule(dbconn:DBConnection, id_actor: str, id_sensor:str, sensor_type:str, condition:str):    
    query = f"INSERT INTO rules (`id_actor`, `id_receptor`, `sensor_type`, `condition_rule`) VALUES ({id_actor}, {id_sensor}, '{sensor_type}', '{condition}')"
    dbconn.execute_query(query=query)

def view(dbconn: DBConnection):
    df = get_rules(dbconn) 
    df_actors = get_actors(dbconn)
    
    st.write(df[['id_receptor', 'sensor_type', 'id_actor', 'condition_rule']])
    st.subheader("Create a new rule")


    sensor_type = st.selectbox("Select a sensor type", sensor_types() )


    id_sensor = None
    if sensor_type is not None: 
        df_sensor = get_sensor_devices(dbconn, sensor_type=sensor_type)
        id_sensor = st.selectbox("Select a device sensor", df_sensor['id'].values )

    id_actor = st.selectbox("Select a device actor", df_actors['id'].values)
    condition = st.text_input("Write a rule")

    if st.button("Add Rule", type="primary") and condition is not None and id_actor is not None and id_sensor is not None \
        and sensor_type is not None:
        save_rule(dbconn, id_actor=id_actor, id_sensor=id_sensor, sensor_type= sensor_type, condition= condition)


