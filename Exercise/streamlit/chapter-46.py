import streamlit as st
import pandas as pd 


st.title("Chai Sales Dashboard")

file = st.file_uploader("Upload your files :",type=["csv"])

if file :
    df = pd.read_csv(file)
    st.subheader("Data Preview ")
    st.dataframe(df)

if file:
    st.subheader("Summary stats")
    st.write(df.describe())


# purly pandas part 
if file:
    cities = df["born_city"].unique()
    select_city = st.selectbox("Filer by cities ", cities)

    filtered_data = df[df["born_city"]== select_city]
    st.dataframe(filtered_data)