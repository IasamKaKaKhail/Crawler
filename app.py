import streamlit as st
import pandas as pd
import pip

pip.main(['install', 'openpyxl']) 
st.title('DataFrame')

#read the excel file named data.xls
df = pd.read_excel('data.xls')

#take input from user
text_search = st.text_input("Search Chassis Number", value="")

#search the chassis number in the dataframe
result = df[df['ITEM DESCRIPTION'].str.contains(text_search, case=False)]

#display the result
st.write(result)





