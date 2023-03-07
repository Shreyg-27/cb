# Modules
import pyrebase
import streamlit as st
from datetime import datetime

# Configuration Key
firebaseConfig = {
  'apiKey': "AIzaSyC_pWSoVUFZm5B4tsmUDo5Mh7YTShZ0bWk",
  'authDomain': "celestial-license.firebaseapp.com",
  'databaseURL': "https://celestial-license-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "celestial-license",
  'storageBucket': "celestial-license.appspot.com",
  'messagingSenderId': "1097565777278",
  'appId': "1:1097565777278:web:46750dde0a58db9f96d72f",
  'measurementId': "G-NMGKYF41BB"
}

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()
st.sidebar.title("Cb 26")

# Authentication
choice = st.sidebar.selectbox('login/Signup', ['Login', 'Sign up'])

# Obtain User Input for email and password
email = st.sidebar.text_input('Please enter your email address')
password = st.sidebar.text_input('Please enter your password',type = 'password')

# App 

# Sign up Block
if choice == 'Sign up':
    handle = st.sidebar.text_input(
        'Username', value='Default')
    submit = st.sidebar.button('Create my account')

    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account is created suceesfully!')
        st.balloons()
      
        # Sign in
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title('Welcome ' + handle)
        st.info('Login via login drop down selection')

# Login Block
if choice == 'Login':
    login = st.sidebar.checkbox('Login')
    if login:
        user = auth.sign_in_with_email_and_password(email,password)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        bio = st.radio('Jump to',['Home'])
        if bio == 'Home':
            col1, col2 = st.beta_columns(2)
            
            