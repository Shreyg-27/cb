# import final_car_plate_number_recognition
from PIL import Image
# import login
from AB.nav import *
import streamlit as st
import numpy as np

st.header("Take Picture")
picture = st.camera_input("")
b1 = st.button("Process Image")
if b1:
    nav_page("MakeEntry")

if picture:
    with open('test.jpg', 'wb') as file:
        file.write(picture.getbuffer())
# while picture:
#     img = Image.open(file)
#

    # np_img = np.array(img)
