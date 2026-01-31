import streamlit as st
import pandas as pd
import requests

st.title("Real time  currency converter ")
amount = st.number_input("Enter your amount in INR : ", min_value=1)

target_currency = st.selectbox("Convert to : ", ["USD","TK","INR","EUR","GBP"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR" # need to change of here of country name 
    response = requests.get(url)

    if response.status_code == 200:
        data =response.json()
        rate = data["rates"][target_currency]
        coverted =rate * amount 
        st.success(f"{amount} INR = {coverted:.2} {target_currency}")
    else:
        st.error("Falied to fectch covnersion rate ")


# deploy a stremlit app