import streamlit as st

st.title("chai maker app")

st.button("clikc me ")

if st.button("Make chai"):
    st.success("your chai is beging brewed")

add_masala = st.checkbox("Add Masal")

if add_masala :
    st.write("Masal add to your chai ")

tea_tpye = st.radio("Pick your chai base : ", ["Milk", "Water", "Honey"])

st.write(f"Selected base {tea_tpye}")

flavour = st.selectbox("Chooise flavour :",["Adrak", "Kesar","mikle"])
st.write( f"you chois at : {flavour}")


sugar =st.slider("sugar level ", 0,2,6)
st.write(f"Select sugar level {sugar}")

cups = st.number_input("How many cups : ", min_value=1, max_value=10,step=1)
st.write(f"Selected sugar level {cups}")

name = st.text_input("Enter your name ")
if name:
    st.write(f"Welcome , {name} ! Your chai is on the way")


dob =st.date_input("Select your date of birth ")
st.write(f"Your date of birth is : {dob}")