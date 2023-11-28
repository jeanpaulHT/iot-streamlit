import os
import streamlit as st
import MySQLdb
from .configvars import *
import pandas as pd


class DBConnection:

    def load_env(self) -> None:
        self.DATABASE_HOST = DATABASE_HOST
        self.DATABASE_USERNAME = DATABASE_USERNAME
        self.DATABASE_PASSWORD = DATABASE_PASSWORD
        self.DATABASE = DATABASE

    def connect_db(self) -> None:
        self.connection = MySQLdb.connect(
            host=self.DATABASE_HOST,
            user=self.DATABASE_USERNAME,
            passwd=self.DATABASE_PASSWORD,
            db=self.DATABASE,
            autocommit=True,
            ssl_mode="VERIFY_IDENTITY",
            ssl={"ca": "/etc/ssl/certs/ca-certificates.crt"}
        )

    def __init__(self) -> None:
        self.load_env()
        self.connect_db()
        
    def __del__(self):
        self.connection.close()

    def table_exists(self, table_name: str) -> bool:
        query = f"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %s AND table_name = %s"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (self.DATABASE, table_name))
            return cursor.fetchone()[0] == 1
        except MySQLdb.Error as e:
            print(f"Error checking table existence: {e}")
            return False

    def execute_query(self, query: str) -> None:
        cursor = self.connection.cursor()
        cursor.execute(query)

    def execute_fetch_query(self,  query:str) :
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def execute_read_query(self, query: str) -> pd.DataFrame:
        return pd.read_sql(query, self.connection)
Dbconn = DBConnection()