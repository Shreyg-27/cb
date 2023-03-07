# import final_car_plate_number_recognition
from PIL import Image
import login
import streamlit as st
import numpy as np

picture = st.camera_input("take pic")

if picture:
    with open('test.jpg', 'wb') as file:
        file.write(picture.getbuffer())
img = Image.open(file)
#
np_img = np.array(img)
