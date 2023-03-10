# Modules
import pyrebase
import streamlit as st
from datetime import datetime
from AB.nav import *
import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb
from firebase_admin import auth
# from main import *


import json
from pathlib import Path

import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages

DEFAULT_PAGE = "main.py"


def get_all_pages():
    default_pages = get_pages(DEFAULT_PAGE)

    pages_path = Path("pages.json")

    if pages_path.exists():
        saved_default_pages = json.loads(pages_path.read_text())
    else:
        saved_default_pages = default_pages.copy()
        pages_path.write_text(json.dumps(default_pages, indent=4))

    return saved_default_pages


def clear_all_but_first_page():
    current_pages = get_pages(DEFAULT_PAGE)

    if len(current_pages.keys()) == 1:
        return

    get_all_pages()

    # Remove all but the first page
    key, val = list(current_pages.items())[0]
    current_pages.clear()
    current_pages[key] = val

    _on_pages_changed.send()


def show_all_pages():
    current_pages = get_pages(DEFAULT_PAGE)

    saved_pages = get_all_pages()

    missing_keys = set(saved_pages.keys()) - set(current_pages.keys())

    # Replace all the missing pages
    for key in missing_keys:
        current_pages[key] = saved_pages[key]

    _on_pages_changed.send()


st.set_page_config(page_title="Project name")
st.image('log.jpeg', width=100)
st.markdown("<h1 style='text-align: center; color: White;'>Project Name</h1>",
            unsafe_allow_html=True)
# st.title("Project Name")

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
# st.sidebar.title("Cb 26")

# Authentication
choice = st.sidebar.selectbox('login/Signup', ['Login', 'Sign up'])

# Obtain User Input for email and password
email = st.sidebar.text_input('Please enter your email address')
password = st.sidebar.text_input('Please enter your password', type='password')

# App
clear_all_but_first_page()
# Sign up Block
if choice == 'Sign up':
    handle = st.sidebar.text_input(
        'Username', value='Default')
    submit = st.sidebar.button('Create my account and Login')

    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account is created suceesfully!')

        # Sign in
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        # st.title('Welcome ' + handle)
        nav_page("home")
        show_all_pages()
        # st.info('Login via login drop down selection')
        st.write(
            '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

# Login Block
if choice == 'Login':
    login = st.sidebar.button('Login')
    # logout = st.sidebar.checkbox('Logout')

    # if logout:
    #     login = False
    #     st.title('Logged out')

    if login:
        user = auth.sign_in_with_email_and_password(email, password)
        st.write(
            '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        # st.title('Welcome')
        nav_page("home")
        show_all_pages()

        # st.balloons()
        # b1 = st.button("Login")
        # if b1:
        #     nav_page("home")
        #     show_all_pages()

        # bio = st.radio('Jump to', ['Home'])
        # if bio == 'Home':
        # col1, col2 = st.columns(2)

# user = firebase.auth().currentUser
# print('Successfully fetched user data: {0}'.format(user.uid))


col1, col2 = st.columns(2)
with col1:
    st.image("Sign_up.png")
    st.caption("Sign up")
    st.write("This is the sign up page for the project.")
    st.write(
        "First time user need to create an account with their emial password and username.")

with col2:
    st.image("Login.png")
    st.caption("Login")
    st.write("This is the login page for the project.")
    st.write(
        "The user can login in the (project name) by entering the credentials used for signing up.")


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):
    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 100px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="white",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(4, 4, "auto", "auto"),
        border_style="inset",
        border_width=px(0.1)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)
    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        # "Made in ",
        # image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
        # width=px(25), height=px(25)),
        # " with ❤️ by ",
        link("https://instagram.com/celestialbiscuit?igshid=YmMyMTA2M2Y=",
             "CelestialBiscuit"),
        # br(),
        # link("https://buymeacoffee.com/chrischross", image('https://i.imgur.com/thJhzOO.png')),
    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()
