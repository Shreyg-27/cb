import streamlit as st
import final_car_plate_number_recognition
from AB.nav import *
from pages.MakeEntry import *
from google.cloud import firestore

# st.text_input('daalo bhai number', value="initial_value")
name = st.text_input(
    "Please input correct license plate number", value=number_plate)
# name = st.text_input("Please input correct license plate number")

if 'count' not in st.session_state:
    st.session_state.count = 0

db = firestore.Client.from_service_account_json("firestore-key.json")


def ent():
    doc_ref = db.collection("license").document(
        "car" + str(st.session_state.count))
    st.session_state.count += 1
    doc_ref.set({
        "Number": name,
        "InTime": firestore.SERVER_TIMESTAMP
    })


cap_button1 = st.button("Enter now")

if cap_button1:
    ent()
    st.text("Captured Successfully")
    nav_page("Table")
