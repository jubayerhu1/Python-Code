
import streamlit as st
from datetime import date

# Title of the app
st.title("🎂 Age Calculator")

# 1. Create a date input widget
# We set the default value to today's date
birth_date = st.date_input("Select your Date of Birth", 
                          value=date(1900, 1, 1),
                          max_value=date.today())

if birth_date:
    # 2. Get today's date
    today = date.today()
    
    # 3. Logic to calculate age
    # We subtract years, and check if the birthday has passed this year yet
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    # 4. Display the result
    st.write(f"### You are **{age}** years old!")
    
    # Optional: Add a fun balloon effect
    if st.button("Celebrate!"):
        st.balloons()