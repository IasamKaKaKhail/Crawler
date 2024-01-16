import streamlit as st
import psycopg2
from conf import config

def connect():
    try:
        connection = None
        params = config()
        print("connecting to postgreSQL database  . . .")
        connection = psycopg2.connect(**params)

        crsr = connection.cursor()
        print("PostgreSQL database version: ")

        query = f"select * from public.\"Custom\" WHERE \"ITEM DESCRIPTION\" LIKE '%{text_search}%';"
        crsr.execute(query)
        result = crsr.fetchall()
        column_names = ["CLT CODE", "TYPE", "IGM NO", "INDEX NO", "IGM DATE", "BL NO", "BL DATE", "CONSIGNEE NAME", "GD NO", "GD DATE", "CASH NO", "CASH DATE", "NTN", "IMPORTER NAME", "PCT CODE", "ITEM DESCRIPTION", "SRO", "IMPORT VALUE Rs", "C.DUTY", "S.TAX", "A.S.TAX", "AIT", "REG DUTY", "FED", "CED"]

        formatted_data = [column_names] + list(result)
        formatted_data = list(map(list, zip(*formatted_data))) 
        st.table(formatted_data)
        crsr.close()
    
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()       
            print('Connection Terminated')


if __name__ == "__main__":
    st.title('DataFrame')
    text_search = st.text_input("Search Chassis Number", value="")
    connect() 





