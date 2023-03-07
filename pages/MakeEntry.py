import final_car_plate_number_recognition
import streamlit as st
from AB.nav import *
from google.cloud import firestore

st.write(final_car_plate_number_recognition.text)

if 'count' not in st.session_state:
    st.session_state.count = 0

db = firestore.Client.from_service_account_json("firestore-key.json")

# for entering data: number will be text received from model-


def ent():
    doc_ref = db.collection("license").document(
        "car" + str(st.session_state.count))
    st.session_state.count += 1
    doc_ref.set({
        "Number": final_car_plate_number_recognition.text,
        "InTime": firestore.SERVER_TIMESTAMP
    })


cap_button = st.button("Enter")

if cap_button:
    ent()
    st.text("Captured Successfully")
    nav_page("Table")
