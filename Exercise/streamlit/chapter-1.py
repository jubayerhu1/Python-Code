import streamlit as st


st.title(" Wellcome to web site")
st.subheader("This is subheader")
st.text("Welcomt to text ..")
st. write("this is another st.wirte( )function")

st.text("Thisi is selection :")

choi = st.selectbox("Choose your language : ",["","Python","Java","CC","HTML", "CSS"])
st.write(f"Your choose {choi}. excellent chois")

st.success("you are chooise python")