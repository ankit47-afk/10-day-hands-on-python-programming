import streamlit as st
import pandas as pd

st.title("My App Dashboard")

if "ledger" not in st.session_state:
    st.session_state.ledger = pd.DataFrame(columns=["Name", "Contact", "Amount"])

st.header("Add Entry")

name = st.text_input("Name")
contact = st.text_input("Contact Number")
amount = st.number_input("Amount (positive for lent, negative for borrowed)", value=0.0)

if st.button("Add Record"):
    if name.strip() == "" or contact.strip() == "" or amount == 0:
        st.warning("Please fill all details and amount cannot be zero")
    else:
        new_row = {"Name": name, "Contact": contact, "Amount": amount}
        st.session_state.ledger = pd.concat([st.session_state.ledger, pd.DataFrame([new_row])], ignore_index=True)
        st.success("Record added!")

st.header("All Records")
st.dataframe(st.session_state.ledger)