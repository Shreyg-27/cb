import final_car_plate_number_recognition
import streamlit as st
from AB.nav import *
from google.cloud import firestore

number_plate = final_car_plate_number_recognition.text
st.write(number_plate)

if 'count' not in st.session_state:
    st.session_state.count = 0

db = firestore.Client.from_service_account_json("firestore-key.json")

# for entering data: number will be text received from model-


def ent():
    doc_ref = db.collection("license").document(
        "car" + str(st.session_state.count))
    st.session_state.count += 1
    doc_ref.set({
        "Number": number_plate,
        "InTime": firestore.SERVER_TIMESTAMP
    })


cap_button = st.button("Enter")

if cap_button:
    ent()
    st.text("Captured Successfully")
    nav_page("Table")

not_correct = st.button('Number is not correct')

if not_correct:
    nav_page('EntryNotRight')


st.header("**Instructions**")


st.caption(
    "Step1: Click on the car plate number which is going out of the university campus.")
st.image("Step1.png")


st.caption(
    "Step2: Click on the Exited button to take the note of exit time of the campus.")
st.image("Step2.png")

st.caption("Step3: The exit time can be viewed on the screen.")
st.image("Step3.png")
