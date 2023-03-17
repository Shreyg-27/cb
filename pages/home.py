import streamlit as st
# from streamlit_option_menu import option_menu
from AB.nav import *

col1, col2, col3 = st.columns(3)
# col1, col2, col3, col4 = st.columns()
icon_size = 20

with col1:
    b2 = st.button("Take an Image")
    if b2:
        nav_page("Take_Image")
with col2:
    b3 = st.button("View Entries")
    if b3:
        nav_page("Table")
with col3:
    b4 = st.button("About Us")
    if b4:
        nav_page("About")
button_style = """
        <style>
        .stButton > button {
            color: white;
            background: gray;
            width: 100px;
            height: 50px;
        }
        </style>
        """
st.markdown(button_style, unsafe_allow_html=True)

st.title('Plate Sense- The smart way to track vehicles')
st.header('Celestial Biscuit🌌🚀')
st.write("Celestial Biscuit is here to carry forward the ideology of problem solving and innovation with technology for the "
         "greater good in our minds, hearts and souls. It's an organization where people come together to build some fascinating and insightful real world projects to help solving the complex problems. "
         "There are many challenges that are faced in day to day life and we here build the workable solutions for them.")
st.header('About the project')
st.write('This Project aims for Licence Plate Detection of the cars entering in the university using the "Easy-OCR" model that detects the car by its plate number and marks the entry and exit time. It takes the image of plate detects the plate number and marks the entry time then on departure of car the exit time is maintained and it helps in efficient management of onboarding and outgoing vehicles.')


# Now we have to add the screenshots to make the app intutive.....
st.header("Working Of Project")
col1, col2 = st.columns(2)


with col1:
    st.image("homep.png")
    st.caption("Step 1 : This is the home page containing the details of project")


with col2:
    st.image("homet.jpeg")
    st.caption(
        "Step 2 : This is the take image option to direct us to take image option")

st.write('#')
st.write('#')

col3, col4 = st.columns(2)
with col3:
    st.image("takep.jpeg")
    st.caption(
        "Step 3 : This is the take image page to take image of licence plate")

with col4:
    st.image("takeim.jpeg")
    st.caption(
        "Step 4 : This is the process image option to process the given licence plate option")

st.write('#')
st.write('#')
col5, col6 = st.columns(2)

with col5:
    st.image("enterp.jpeg")
    st.caption("Step 5 : Make an entry by enter button")

with col6:
    st.image("entryn.png")
    st.caption(
        "Step 6 : Entry not correct option to correct the entry of licence plate number")

st.write('#')
st.write('#')
col7, col8 = st.columns(2)
with col7:
    # st.image("sunrise.jpg")
    st.image("correctentry.jpeg")
    st.caption("Step 7 : Enter the correct entry ")

with col8:
    st.image("tablep.jpeg")
    st.caption("Step 8 : This is the table showing the entries of the cars")
# import streamlit as st
# from AB.nav import *
# st.title('Celestial Biscuit🌌🚀-Team:26')
# st.header('Licence Plate Detection')

# st.write("The objective of this project is to develop a well-organised system in the vehicle number plate detection. Methods: The major techniques used in the implementation of the designs are gray scale conversion, black and white image conversion, filling holes, border detection and image segmentation.In this project we Take image of the car and search for the number plate in the image. Once")

# b1 = st.button("Make an Entry")
# if b1:
#     nav_page("take_image")
# b2 = st.button("View Entries")
# if b2:
#     nav_page("table")
# b3 = st.button("About us")
# if b3:
#     nav_page("about")
# # import streamlit as st
# # import streamlit.components.v1 as components
# # components.html("""
# # <!DOCTYPE html>
# # <!--
# # To change this license header, choose License Headers in Project Properties.
# # To change this template file, choose Tools | Templates
# # and open the template in the editor.
# # -->

# # <head>
# #     <!---- The page has a title Lifestyle Store-->
# #     <title>Lifestyle Store</title>
# #     <!---- External css file index.css placed in the folder css is linked-->
# #     <link href="style2.css" rel="stylesheet" type="text/css" />
# # </head>

# # <body>
# #     <div class="header">
# #         <div class="innerheader">
# #             <nav>
# #                 <ul class="navigation_bar">
# #                     <!--                 <li> <a href="#Lifestyle" class="logo"> Lifestyle store </a></li> -->
# #                     <li> <a href="#Signup" class="link"> Signup </a></li>
# #                     <li> <a href="#Login" class="link"> Login </a></li>
# #                 </ul>
# #             </nav>
# #         </div>
# #     </div>
# #     <div class="content">
# #         <div id="banner_image">
# #             <div id="inner-banner_image">
# #                 <center>
# #                     <div id="banner_content">
# #                         <h1>CELESTIAL BUISCUIT 26</h1>
# #                         <h2>Licence Plate Detection</h2>
# #                         <input type="submit" value="About Us" class="button">
# #                     </div>
# #                 </center>
# #             </div>
# #         </div>
# #         <div class="para">
# #             <center>
# #                 <div id="para content">
# #                     <h1> About the project </h1>
# #                     <h3>The objective of this project is to develop a well-organised system in the vehicle number plate
# #                         detection. Methods: The major techniques used in the implementation of the designs are gray
# #                         scale conversion, black and white image conversion, filling holes, border detection and image
# #                         segmentation.In this project we Take image of the car and search for the number plate in the
# #                         image. Once the probable number plate area is located it is given to OCR. If OCR doesn't
# #                         recognize the characters from the image number plate area is searched again from the image. If
# #                         characters are recognized then number plate search is terminated.</h3>
# #                 </div>
# #             </center>
# #         </div>
# #         <div class="container">
# #             <div class="item">
# #                 <a href="#">
# #                     <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxUUExYUFBMWFxYYGBwcGhkZGR4aHhsbHB4ZGxseGxweHyohHhwmHBshIzMiJistMDAwHiE1OjUvOSovMC0BCgoKDw4PHBERHC8mISYvMC8vLy8xLy80Ly8vLy8vLy8vLy8vLy8vLy8vMS8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAJgBTAMBIgACEQEDEQH/xAAbAAABBQEBAAAAAAAAAAAAAAAFAAIDBAYHAf/EAEwQAAIBAgQDBQQHBAcFBwUBAAECEQADBBIhMQVBUQYTImFxMoGRoSNCUrHB0fAHFJLhFjNicoLS8RUXQ1OTNHODoqPC0zVUVWPiJP/EABkBAAMBAQEAAAAAAAAAAAAAAAECAwQABf/EADERAAIBAgQDBwMEAwEAAAAAAAABAgMRBBIhMRNBYTJRgZGhsdEFInEjUuHwM2LBFP/aAAwDAQACEQMRAD8AvYG/YZltrcN122LNfXWJbUYcLA1100HKvOLXURjaFtS3d95Heu6sNYGqjSRr1Hy5eO1d3mR8B+Xzpx7WvHhs4ZTESLK7epk1nlSk42TszRSrU41E5Jtd2wV7O4kMSIE5hsI01GkfVB5fyrTCyf0tYfgmKAuWsqkksAxEQAsEmANN63tu7PKp1FZjwkmhKkf6VZw9vM0EgczLBdOcE6T00NMtiSBpr1MD3nYVexFzKvdqxjd4YMrHTaANB0k0g5XxV7NqScqiBmI0A6kAD5Visfwx8cHvZsirIsKdAyiZZumY7HyG4rScbuW8mW5cKAzouaWEagBfFt6jqDVa3jg1i4VylBmWMqn6MkqANY9nqJkEbimUnFZkK4qTysxPZDidxMQqakXCFIn4Een3TXTLYrHcJ4XatFGVbtx1fOGVAxIgqVJ2AghoGviFbHB31uKHUmD1EEeRB1BpqjUndC04uKsyWp7Cp3dwn2/CE1I5nMY9OvWomrwCplDw2zTe4J2BI9DUhWa6BwTFG3ZwtsWncXMwLJGW3AZszkkGCREgHU+kvCGZ2EnLKjA9z/8ApPr4vzppwzgeyw9xo0nbu+x8K2SBbdycpgSt25aB+kBB7sJMAyQ2qyI02M4zcREgKzd7YVrgU90wuYhbDhfFIuAEmDIBI1NU4PUnxuhz02G+yfhU1+2oRCJzktmBnYEZflWvwnaK9msZhacXc+loHMwCXnQpmfZ+6IUkQwBJKGFMHa/EG5h8O5ttbLmSjgBklZysAdxzFCVKyvcMat3YyDJVa5bq6qZiAIHqQB89Kc+BP27f8YqJYHhamVa8uWsu5U/3WmlbeuOH5eu1S4zDhWIVgy8iOYO09D1HUVCxpA+6gGw17c1WuLG9XLz5VJAJIEx160KucSkex86KAyzw24TiLWXRcxn/AAhy3v0Ue+rNjtbdYtm7pIuMuiloCsVknMJ1FecEseEyW8QczoSO8gaacvOqS9hLOn01+BOhKEGevhFeRKvh+NJ1uWi36muVKtkjkIcDxkX7+d+7V0ViPo5DZczGZaZgfGKvf0wgEhrJaDCspExyHiqD+gtldr92T5KfnEVDc7DWjvfun3J+VVnX+nSSuvRklTxn9sW8fbDFXC5c6h8oMgE7ge+aosnSjOF4R3dsW1cuLSmWf2oJnkNQJjTbSo24axCkRlcwGkRm6En2ffFacLK9JNarXyT0BWjlk0/7oCRUoIOh35HmPOrd3hF0MQbTSOWmsdPtHyEmqdzCsqqxU5WnKeRj05+W9aSSGXmA9rQfa2H+LofPb0rxrKnST6U8ABS7yLY9pokDynqaqi4jS2GYugOqnkd4B5HnG3pvXZXuHMtiQ4cA6GsHeg3WHXb+MfhWuuFzJD6DeQAR6iNKzGP4Y4JKiZO8iI5++arS31JVdtBj4q/cuIotks7DIMrePQJprDDTlWk4VcuYcXTeuW7LEZSr2muyUJYABSV1j2jIgyKu4Am3h8PcGly3bQI2pKd5edGy6xqumxoZ2nxVg9+t5bhuC4wsMrQq5TlIIgyuwgxz1p7R5IVzm73YM4VirtxcTcNwnNZc3QZ9o6IV84HlpIoZNEuzrH93xihZ8CHTl/WevWg372vn8KqtNjDXUpWZdHZXE/8ALj3iprXZHEH6qgetdq4lwi0hyo7MR7W0Dy050/hfAhcOshRuR16DzqHFlext4UbXOcdnOy7WZZ2BJ5DSP1+FadcPR/iHD7StlTMQNyWG/QR0q7wThKu2dlGUddQT7+QqbvKRVZYxAjYfulhswuHUDwkR1O5neoTfPX5D8qKcWs2g7d2kAbkbE84jYDapeB8EW4pZwYOw116+7+dCzbsg3SV2ZlgWUkEasc8j6oZlAHuAPTVutB+1eHbuGFpWLscsJJJWPFPQeGI8hGprU8X4BhnulhaUxAk6zG09R0maK8I7MWnQtdBIJhYYjbcyD+oNNHfQWW2pg+C27VtLaC6ttrZh0LD2mAzAlwDqxmRp0mj9oDU9T56wAJ122+EVLiOD2O8JS0IB8JbUxtudfP30e4RwS0yS67nTU7D9Gh2noHsoCYPDm44QETrqdhAkk0yr9kqrOUEBgV1nRT794onb4VaFrO4Psk6EDTcUErhbsZtxPM/r1rRcL7WNatLa7oNlEA5okT0y0CYAbfjRyzwa33HeNmnIW3gcyOXSug5X0BNRtqPXtRbnN+5280RMiYiInJtAiOgqRu2AChRhlyiIXNoIIIgZYEQCPSs4LQo5e4Kgs5yWkKDE6SeXzp1Uk9mK4QW6LHDO0qZ0VcLbTUgFSBlzatEKImNetU+N8YbFWge7VVRhPikywMchpvVPhWHHfJ6/nRHEcMVMO2VmM5SZjcbcvOuzSkjssYvQzkVG4q4iKetQdocbhMOUS5dfO+qqEdpGo0yqefKpJN7FG0tyoQNdq8FDx2nwZ1FxyoEki3cMLME+x5HXyq3je0HDoAtYi4znUKbVySCCZH0eu1MoS7gOce8s7U8ChA7R4QMM1y4BMT3dzeSPsbyCI8qnxHHsGolLtw6wZs3RGxGuSOY+Irsku47PHvCly0V36AjWdDttURt+VD8B2nw997dhLxJJIUlHGntakiIEE/GjnFuHtYglpnpQaaCmmBeGlrl1TbMQ0uM0SgJGUDmZ+41pBbA6/E1yw8YvYVzB8PeM2QwuZcxMTJMAtuIPlVwftJf/AJC/xt/lrxsZ9Mr1JXpq6/J6FPHU1G03ZrobXi/Drl1l7q+9kCc0Q0yRBM66a1VPZq/H/wBQunWICAadZIrLf7xj/wAgfxH/AC03/eMR/wAAfxn/AC0aWExcIOChF9zdroWeJw7kpZn66m5sYW415yHIhB3azBLD245gwRHXWob1x4ZZaG3AMT69azPZ7tC2Ku3GJKKqplUeKGkyZ0OsD4Vqrr5vFprvpz+O9ejQpSpU4xlo0Z61RVJOUdivfwmIXIRduwR4CrSInaY5Hkdqc4xAd7ZUsxXMylVOcDXNAEMf7Q1ohw7Du4a0txROuVgSNOY6HzEVFxCxeSLbFQVOZW1keasTIHpV+pHocu7UcRuXbjlEAtWCFcroM7TvrvII/wAJqlw/GlbtsrPeFkAA+tJAI6agkfzrT/tCsoLKP3doOzkl0QqZUalgPCS2bfyrO9kOFPexNtoGW2VuHNswBBAA5yY91aotZLmSSeextcdZ11V1cbaQfeI2qojLOW4hUn60EKT012P6E1rrPC3vKcqWpGk5ipX0UACKo3+FuD3dxQJ01On+lZbGxMC8VsXe4VbNvOz3LdpNRoyF7sknYAe6sLirzBnV2zsrsCZkEgkHXmCa6PxPsxeW0ygk22UiR4ikiAwPT8OdYThHZe9iTcW01sm2SCGLZm3MhVVjBg786vS21IVnroEewttLq4gOoOYqCNQCsNpodpnbXzrMPasqzq5aVdh7gSB91bjsxwx8N3s2rnjygZlyMAsgyrQQcxNCsX2Ke7ce4GgO7NBAkSSY0aKdVIpvUm6baWh0nC8btPHtCTqIP3gEVo34wAmS2uTTeZI68t/Og7T+pp41rKpNbGlxT3Hqeu1EL3GPBkRMgiN5gfDfzoYBUV24FrlJo5xTPLjTpPlRg8a+jyKgURlHimB8OlBbYnepctBNrYLinuOJFErnF5tm2qBRESDMDbpvFCZ9aTv5H4UU2tjmk9zxqIXOPHu+7S3GkTmnTY6RzoY76VEbmhMbA/Kgm1sc0nuSo08qKYzi2e2U7oDQCQdgI8vKuf4HtZfui2UwiE3ASim8AxUZxmjJopZGUHrA+sJmvcfxSsifuSnNba4IvaBUUO2YlNIBHkSwAk6VRU5om5wZfv3PEdDNHz2hDWO6FsLoFkNO0co/U1hMB2ju37ZvLYsBASGL3suWANWlNBqPiKvXeI4pJD4O2kTvfHJWYwApkBUf/puNwAe4c1yDxIPcODEjnRu9xzPbKZYkATPSPLyrnHF+0d3D63MIkZ3tyt6RmTRvqTGYMAeZRo2rQdneIjEWFvFMklhlnN7LEbwOlK4yghlKMmGsDiMlxGbYHWP9daK4nHkWshTMpWA4Oh0HkIP9k60BF1RoSBpVjD44LIDDXdTqG9Rz/DlQjKwWrlcP4jyHnWf7UYbEXL1q5atG4os3LTEXUtsM+kozHwtHOCNxzrWG2lz+qIzH/hkyf8B+t/d39arZhl/xfOpznOFnG29tRlGM9GZPvMeEKLw9Rplzd+hbJkdYJZjLZ7jXM3VmkGSSObhWMnC3BhX7zDFIJxNohkRi5BIIiSYnkBqW5anjHE0tFUBm485BqR5Fo2BOn+hqLhVp71sMpJbLJz3FQMJb2VEEkkFdo8PKrKdd6/b5P5JOFJd/mgThn4miwuEBJUA5r9thKoiKVUt4ZCy2sszEyNqcj8RUyuDkg5kz4lGhpvkloZc39ewG0BU3iaIcWs4iyJKjT2vpMwAIENIgBSZHqD728PxNy69tFUHvFLBu9YAZdGB01IIjTyo5q/8Ar5P5BlpdfP8AgznZ/sriUxiXWsd1azXDHeI2QMrhV0aTEgTFdOx99blkI8yNiAN+WszFY/C8Ua25F0sVNwoTmQqrSQMsePKY3bqPStH9X/F+BqFWdVNOTXJbMtTjTa+2/mYjtF2Oe84dLgHkZPnQR+xF8fXT5104VEy1VVpJWJulFu7OXt2NxP2rfx/lTR2Rv8ynxmumG15VE1im48wcCBlOy/ALthmJZTmgQPKfzraYfMN4rmmEv4VLl8YlFYjEFh4WLFVF4sgykAA3FtDUjRmgjlPjf9m5EW0Vzi6gLsl2DbB1YqDqO7yhlEEuLmXQrVXRctWxFWUVZI6hbA0INETjluJkvGY2YDUfrpXFrb4FL15nUPZdQbKW8zFQboBBzZYfuwWgyBmHPSidjFcKiHW3n+kJZVv93mBt91APjy5M0iPaDcspIWHtzA69+QV/aMQLVsSChuEEnTdTB68qqdh+IIcQov3mVGtNtJGdszFiOsxyjf1oFw3IcTfOGHhFvwaGAfCHIB8WQsWgHWCJ1q1hsKiYq2VUhT9Q7ewQfmB8aNsqysF7vMjpKcQVW8FwEg6MNJ+MfCjgx9q+kXvCw2YA/KAfhtWIVZ+qsRtln13qyFI2+A/CsqlY0uNwtxXF93ae2GFy22UMusMpdQ412lZB9edcx4Zxa5YYWFdkW7cTvGQ5SU0BUEagzPPmZrY40OUYZSZBEDnv86wmJwLOWd1u22DAglCNJJJny3q9FqzTIVU8yaN9jLxtMyLDBGZA5JYsFJUEnzjmTVb/AGjc6J/D/wD1QXhX0dm2DmAyjeYBPLyq/wBzSNWK3ubqKXvrwmm5j5UgRxFVShY8oqdnpsj0rgjlWvTtypKelIxQOGKlIz5U4tXitXHEF9egBofcZ9RqJkdR0J1FFi+lRO2/500NxZ7GK4f2YxVu2q2sbkWAARbAYDN3gGec2XMSYmNT1NSXOA40N3hxzT4hokaMAGWFYDKQo02BEiDrWn/ecllW55QAOp0iouE2b2KtIQTHf3VZg0QuhBHXQnTyrbKvaTSitH1MkKN4qTk9V0+DJ2ezd9S2TEqod2coLK5CW0IyElcsbLsIHQVOvZTFEMP3yQwIM2wSQxultSZBPfXJYa+NhMGusYLhVm2o8AdgILMJnzjarq92NBbt6csq858vL767ivuXr8g4S/c/T4OMY7snirqlbuMzKWz5TbEZpc5gAYBJuOSRvm1mj/Z/hz4awtmFfKWOacs5iTtr1610i4lsjW1b/hH5Vz/j2JbDvaQnNme7MCJChIiTIjxUHUvo4r1+RlTtqpP0+C2oR1UlRqJg6xU62lG0fAVUwo8Cegqc9Ky1YqM2lsmzRSk5QTfNI8u2VLAzrPxqfG4jMn0jxqALmxB28evjEkDcHzMRVVyeutU+MknD9JuLPx0+YBqFR2t+UWir3/Bhu0i4lSRdUNmgLdRs6uVhYR4HiGUShhgWYkCaMYHGY3Cwtr92uhZAa6jZlmMwBB9klZqx2exCd/czMSntZBDIzowEurCGhvEGGVhBIYSaM4vhVtiFw960SRORmJuDSfAFB7wRrHtR13rZxI7GfhvcHjtbxL7OB13Hdv8APxVV4jx/iNxAg/dVHRUZREbe0dPhVPFaAsuNwhHnc/AJ+NSoyg5Ti8KzACSHZVJPQMs05LQCXkxBV1uJh1BUEuA2bKGBIQA7yAYPQRvWs4B+892WuXVYG+eYP0YVxA00OaCPIUG4nbU5WGJw+XWStwtp5Qu8jrRrgVxO5At3GuA3AJZQuoRvZEmZy/E1lxNTRLqjVRpNataWYbDimswqHujXoSkGPHIpBwf9aY1uaia0aK3Oex4ttYJgTJ++vUtp9kVGh841MfGhV7jlu3fW2bZuCRmg5d9PCeZ3+Fa69eqptRb/AAjHRoUnBNpbbsMNbX7Io3gOH2MuV0GbIWnoNIiPd8akHZ62QHR7mVhmALA+1tMjy20+dBe0uOvWkSytlmzHK9xEdotabBRBJ6ZhGUViofU3Um4Zmna+t9V0NE8FTSvlXgRqbRJCjQdRB9d68ZU+yB7qzOFxDpdQJbvuGJD5rbgqJABHtSfLSPOt1iezTopJJPrAOvkPvp6uOlTazSevPl4nQwlKS0ivwDMPeUCPM/fU/wC9CqaYbntqR8CalGGH6NUxDvUb6i4dWppdCc4mR7VQXL/kTSNlRqaQVKgXKOJvMQRk0PMVWtIY2NFntL+v1vUZtjpTpitB8vTHc704r1qK4y7T8DXHDQ80i1OF1QByB2nY/nTlvqdiPdQOGLcPvpSf0asZBSyCuOII5U7J5VKqCnRXHFZ0PvqDFYZjlykQrEsJK5hlIAkDkSDHOKt3Br8ZpxtmJCmCJ5D0p6faQk+yzneLxd5Lvj/qA+fSWMd2LYAB2kgkf2p99fst28/cxkZGuITJE5YI5rI31M9YG0VJiMWbt3uAWzLeBPlbQZ+nsyBp+dH2YNoYMeVbKmk3dc2ZaavBWfJE4/bFh/8AkXvjb/OoLP7U8ILr3hhr+d0VGOZPZQsRpP8AaNRG0n2V/hH5VDcW3zS37wv5Ul13D2YTb9sWGG1i+deZQae4mszxXtsmIuWyFfMLgjMBCJrOXxHxEtry8I6wCIsWj/w7Z/wr+VS3MPbNtlyoIVmGgENlI1jyJoxauLJOxUfE467dIw7hFtqBD5crwzbeEnbKDt91bdJgTE6SPPyrLcD4iv7w1kCfCWJ6HNBH3GtEHNSxT/UatzZXC/4k78kPvqTqDsaFdqrpXCkruLlvz+sulW7t0+dAu1xLYN1B8RurHqozf+2skt4/lGnk/wAMwV/GEEn7QM/4jm++rx4tcvBZuKgT2RDb9QVU66DU+6htrFqshwIK7ZQfFy35URsd40PawilTsyWr3LzttB91elsefa+tzS8K4jbvC2165Ze6FObPbfM3m7BSGcAe1EmTJNN4jjcK0RdsIw5qlyT5aW9ue9AUfErthCP/AA8T+LVHca83tYSf/DxH50jpRcs/P8v2Cqk1Fx5FXjF8Xbly6jIEDBVWYYqoChgsbGJJ6k0b7PXz+7oZP/brQGv9hj+vWgt1GGrYRQBzK4iPeS4FFuG31OFRlUL/AP77eigxOR4iSTHvpK60KUd2+h0Q3KQuUOS+T+pqVHasxqHcT7wp9Cyh5+sJHnU1nCiPFeaf7qj5Rp6SfU1GpJqWDrRT1A1oVL3CO+tsEvlHDGDAMQZE/I6etY/iHC7yXxbddSVVSPZPiRc6zsJIGX0rV4K4VvNBmZaPM+D4eD760hRLgTvVXQgiRz5en8q8/G/UJ4fEzUtY6270Vw2FhUoQa0dteoTtKpBQgMmULBEgiJoKexmFn2Gnl4pj3RR3ulicxU8+YMc9jy5VA15R/wAT7vyqeG+q4enTjF30XdcFTDVJSbicr7d3Ewl0WsOCt3R2uayn2VtzoOZLDXUajasgcdegnvbsnXN3jSfXWTXdMfw7C35N9Lb+GM8KWUagQ3LcxWZH7OsAR/2y9HmbX+WvQpfUsPPn5ohPC1lsD+GZ37u6LzGEXvrZ1DMyllccxOuvVDRS1fY6R76scL4FZtF7lu9cL5e6CysFUbwNoAc2nLTU9a8GLYOdW0Ma8/nTzrwnWnGL29g0KUo0YyaI8xPKo2B6Hf8AW/Kn3sddnZfeAfu1pW7l1mhjbUdY/PQV1h7jWVh9Q+v6NR94eny/lV28Mm6hj5AD7qhJB+of4aAQ7dM6RTBaAIOmYbEiY+O1eq0xSy0whY/fCRGYfAflUARZmBJ5xXleRXXOsPzV6WFR17XBHBhTbl0xpvOleFiKiZpMGuOJQ0aUy9eIVjqIB+6mM2tU8ff8DDqpHxFNT7SEnszBXsclm9duBSX8SmTpE6x0MAbzty1q9fvObS3E7pQzAB7rgKJMeIggj+VDb3BFv3Lrd+FcXH8BXaNjvz60NxnACGC2XN06ZhkylJ2zAEwNOdbKkXxHrzIU6kHTVo207+febfC4RHyj99wJYwIXENqeg8E+6ifGOyNjImdcKLxAOa5iG8SgEtCm2DHPyFc64NgGs37dy/bzW1JzIHUEggjTNI3I3rUcS7Q2TATDsQAY7y9bJG8QB0qNRyi/tV/GwYZWvudvC5Df4bZsgul3AEqJi3iELGPsgxJqlj775ELpkR2G7N49jAIXUEedZQ8Nf+z/ABL+dEMPwrvGUWwoIILE3laIiZVRoJBg+lVUdVqJmjZ3Qb4Zd7rHyr6vcKsDA8LQBl1ljmIPu510AJXM7dg/7RGoMXQ+hmBEgevlXRUxc/r76li1+q/yUwjXCVlbQ8xIqpj7H0BB/wCZ0/smrGOxAVS2aI6x8Klwi97ZBGoJkajaN6w1mopN96NkFe66HG7PELti8zWrjW2lhKmDE7UaHb7FCPEGgc2u/P6StlxDsiLhJyj5fnQnEdgCdp+X51rWMovdoyPD1VsmBv8AeDielv8A9T/5K8/3hYr+x/6n/wAlXn/Z7c5fev50w/s9u9fmPzpv/VQ/cgcCt3Mp/wBPcUfrKPfc/wDkq7g8ddxGFQ3XLkY23E8gLdxo9K9H7P7s7af3gfxo3gezJtYfu20Pfhxz+oy8vWo1cRSaSi1cpTo1E3mT2LmHuHzohbaANeQ/0qHD4LKKtix50tyh53h6CPXWabexUTuRUptVHes++uT1Oa0MthsaBj7igwWRTHU6/OCK0/DcSb9rfI+ZgDEgFWZRIOhBA1HmYrK8c4b4xeQRcQ6HrBO/lWj4Di5RWgroIHqoP3kmsn1ql97qR3TXpcv9KqfpqD7ibHWsfbQZERiCcxUxIiNBKxG8DmKmwHEMSIFyypYgmXLZIgREMTmmdZA12Ohqa/xS5yBPuql/tN59g+4MB8q8eFapKP3Qi332PYlDMtUl+LovYqzfuZScJh+qnNcIHrrp86G425iFDp3NhX5FSTEb+1IMjSnPxlh1/wDN+dVbvGWO4+TfnWx1s0UlTSa/uxnhhpRbcpNopvi8USqKtwCJd7YbRjMqPEF3+FXODPcysLoyvnOkkkA7aknXnvSfjLKoUDz58yTT+AcWt57jXbYcMdeo5gjX5Vvbk8RJZUl0M1ksNEuMNNK9KVJiIuPNi3cy6aZZg9BE6VZscIvN/wAMj+8QPvNXszFdFKfSP1yp3fevwounZhz7TKvpJPxEffVxOzQj+tP8P86OSQMyB4Sl5VIxpjcqJx4RSil8KcT91ccNryKfBNMb31xxGxphp7LrXlxa44geKE8SeATFFLw0mgXFgcjR0podpCVOyzLYzsjirrvft2bhVnbKVRzoDEyFiJB58qGX7V7DOfpMQjbFgty1MbeIkE+UirOKZRde4uKu28zEwEuCJ8wRSucWuFDbbil8od1IukGCDzbqK9SdGTk2mrX70eZCrFQSaaaXc/gpP2kxQ2xuJA/767v/ABU7+lWL5Y/Ff9Z/81X8Jxu5aTu7fE7gSZy92xEnc6zrUh7R3f8A8k3/AEP5UOBLp5objx6+T+Ab/SnFHfiGKHpdf/OKqJeuXrmt57hLAku5JOo1OZtT7zRW5xVmu9+eIuboIObum3AAGm2w6Vd/pXf0nit2OgRhPwoqjJbW80B1ove/k/ggsjJj2ndmJHn4Sf0K22GaawFvHNexofOzqshCZ8KBWygTsATt51ucExgfryrFi9ajfVmvCK1NLoi1f0AOUNBBgiRPmDUfCicpUjQbbj4TTrsx7x99e4YyNJ0JHPaazGosmmOo9akr0xFCyCDblry1pnd8hQfG8cuq94BLeS0yrLM0u7KzIihQfEwRonTSJ1FWeInF2Vd7tuyoRgrHO4AzdzrmyZY+mXnOjEAhTVFSbJuqkEVtDkKt2F+dZmxxW+b74fJaFxFLatc1AUOQBkzBsp1VgCDIMHSr4xGJVS2XDZFDlm71tO7zhtMmYn6K6RAMi08TpJ4MjuNE0iD4U5NKz2Jx+Lto7d1ZYJbN1gr3NFUkblANQrMBOynyldmu1tq8jNiM1mHCgohuKZE6tyO+nQGldKSDxYs0g99eZZopwe3hrrMC7AiSAxC5k0GaCNNTtOxB50ZfCYZFzGCORksJ57aUFTbOc0c/vWMyn1b7zWGx93GWr7m0lzLAUQucFVEDSDXZ7yYKSe6Zp10LAef1hVHEXsN9XDn33X/OtU+C23Jtp8rJ/wDTLDjRSSS053a/4caxXG8X9YFfVI+/X51GnaPEDdh8K6fj4+ratj+Nj82jes/iMFcn+sI9FX8VpFDC7W9F8lHVxfJ+r+DHt2lvfa+f86Ye0N37R/iP51s8NwXE3Z7pnfKJMIhjl9n5eVUzgr4JU3SD0KICPUFadU8L18v5FdfGdPP+AHxvi10NbAYwbdtjvuRJ51s/2f8AaGzZsfSWy11nZiQF20A1JnlPvoJd4CXbM7FmgCdBoPICr+B4Lkpa04NtwQ1GNRRSk72OkcE7RpiHKZSh+rJnN1Hrz+PSvOL8Sv2nIGUKfZOXcecneshh7BUgiQQZB8xG1bnh+JTFWjbfRwNfwZfxH51nleasnZmiOWMrtXRn34rebe43uMfdFQG432j8amxuCNtyrDUfAjqPKoSK8+cpJ2Z6sIxaugjcaDUWeT+tKfcqILW88ommlMjaoHvopIzCem/+lZ3tNxi5msW8NdQC8l1mbLmIW2oaUAM5oVwBzIA0oxi27CuSSuaO5irayGdRBgyfvqG5xawu91fvrKcM4dij4+9thbvJ7URN1LVrMjXAVLh843MLpmMVmcZxC8VtXXdSuIGdilsnu5uPbI1IEypMSB51XgsnxUdJbjuHiTdjzhvdyqM9pMKf+NP+Fj/7azGJ4XczODibYyHUtaKghDeVjIciQuGuuV5wBuSFhTs1cGb6YTn7tvoYAyki48m4PAqozZh7QB8xRVEDrdxr7XGMPcMLcBOugDcpnltTcRZVhPigjQ5Gg++NqxfC+JXjxO1avW7JZbi23hIDi1pmiYJZV3jXQ13XiP8AUOFjwiQBpOXxAe8ae80rpNDKqjknEOzQkgggjr56/MEGhN3sgCdGFbzj90Wu4Z/Za3cQtHOwWAPnNsfIUFwHF7GIZbdq6pZzCqfCSeQGaKF5rYNoPcydzsaeTCmN2Lbk4rqVnsviCdVVf7zD8Jq5a7HvpmuqPQFvvimU5iuEDkP9Cm+0Ks2OxpHMGuyW+ydse07n4L+BqReGYS3uVnzefkDRvPmwWhyRy7h/Z3u+lH8Lw/oCfQT91bQYrCJ7KqSOifiRTj2iQezbY/AfdNI0nux02tkZYcHukT3T9fZPL1qxgez96D4QACeY9dhWjwPHDduBMgAM85OxNDsdxa6ruoIEMRoNdCQN55AULR3OzS2I7XZdzqXA9AT+VB7mLwtt3RjeuFGKtlVVGZdCJJ1g6adKu3sfdO9x/jA+VZXj+ECjwSGu3IMHTxEm4w0Ou5nqSaKyvQ55lqZ3i2JtJefEWL2ItLeCOAuWQCpKzrGYQRI2k9aq8PGdrNsYq+gkC2Xy5Vm4rbydO9tqfVfKoeP4UAWgmYhVVYPIS2SfM5SPcBzqO4pcKlu1qmZgF5h2DD1gtHXlXozqKDyqK5ex50ISkruT5+5rrXYa9fBuDFywR0YDKGAYv3isFX2iSwM68uQq1if2e4oTdbGsSIYnMfqhxzWNrj76HO07moOB/tIs4dStzC3RdIXvCuUF3AgsQxEEiD5mTRVf2tYY6fu2I130t/5qTjP9qKcH/Z+hlMVwh1uvabG3CyIbp1BB8NxiASNWy3Lmn9o9ah4Twu2guWA7EXBOsDW34wQRzgMo65zV7jPEsNdvNcW/lBiAbbyAPResms9d4wgY6MwGkxE+epBg0tPExnpl9GvcNbCVIWbl6p+xp8biO6tJdRpayU0n20cIkeYISfnWh4T26wc3LFx3AbY5GIzRyyg+XwrC4riFjuEDW7rXnt/R5YyrOYCdZJzRtyFEeyvA7F5c75hcB8QhSQIA0zKY2Oo1pMRGMZN27vVD4eUpQWt9/Rm3QAiQQVOoI1BB1BHUEV4yeVXsfgkVbZtLlthVAEzoBAGpJO2/lVbuz+tKxNWNiZSvqKrnC5iFkCdNTA16npV27b5kVDdTypRjY8JsWLNsIlxCTqxzDxN8anxvDbd3V7asYIkgSAdNDWBezWw7NcS7xcjn6Rep9pevqNj7utWjJPQjKLWoEx3ZNlk2nDj7JIB+Ox+VBUsFSREHYgz8K0fa3gwB79Bv/WAdeTe/n8eZrPotJJWZSDurjkQVPg7xtsHUww5/rl5VEqjz+NSC0D1+NKMa4hMVakQHH/lP+U/raszeslGKsuoOv6mlwzFtZcMs+YncdK2S4e3fAuaNI5nUeR86EqSqajU60qWm5k21NIJ0omvALp1JRff+Qq3Z7M/aufAfiTVcjI50YDiOAu2VZle0AWLSwaZdiYgaFpMbj0rJY3hhRe8vy3d5Vtm2xVoEGSOWrA+paus9q+EJatIwJMOC8kbAMRoB1j41hRje8zyPErFSI030P66Vqw8mpaq9k/Yy14px0drte5n8ZgrNsgsbxLmSe8MnKRBPUgnSj/Z7sVhsXaItX7gAIL22kZSM2UwGMjxNB03ahuNw4uXGkEi3lUAGJlbjxPKYVZ86T9ncTaYPYxBzgRoTb9YInTyNOsQ2uXkhHh0nz82an/dZbOhv3Ikndt2HiPtbnY9agwf7NrV20lxb90q9tIBLewRoN9grERty51nSeK//AHF3/rD86q2cFxBQAt26FAgAXzA8gA2lHjy6eQvBXXzZuMB+zm3YvW763mLo6wWUsJ9kT4tRsK1UXQy2LjqyXUcHKpUjKqjcseVcebAcQb/jXP8Arn86t28Hjijh79zOcuQm8xK6+OCDIkRtvTQnnbUrbPkuSuLOGVJq+65vm7Gm/aZxdbS2MMh+ktl7hYHVSxMaR5nTyoTw/sXhrb2rq3LzqjK4ByrMQwBZZ5gbUO/oe3d3LrXme8Jc8wwAlpJ1LRzrQdlLrPaS1lJYEoI8tY+H3Gsk20tGbIJN6o1t7tNeb2Qi+6Y+Jqnc4xfbQ3WH93w/cKO4Ds0qjNe8TfZBMD1I3Pyqpi+zTLJQ511gbEfHQipuMyilABlmb2mZj5kn76ktpTr1koYdSp8xSRqnYe44LUgSvEipFNGwLlnhA+mt+v4GmcYtxeuDfWfiAan4Yw723uPEPjS7SowvkiIYA7+UfhTW+0W/3A5hpQzilqWtxAJzAE8pUiRPOPlNETcP2fgaG8bukC2csDP8NCPxj3ilQ5l+0GE+mMSSVAmNWJJZgRsfEdqZ2awwhniJMaCPZGunqx+FGMXeAvOxgEG2y9VY95MH1+6tC2PsXiO8yyUMMAAdCJ1A39RO9VxFfJUytPVLXwJYahnp5k1o3p4gQoDrGv60py2zSxjYYMQuJYSNgBp7zBoJdFksw/eGIUxnyqwPmCDJpYTUtEPUp5Vd+4cPmTTSdKE8PTD93cunEnOk5Vyxm0kbud9tP5VDb4zb0m68/wDdx/7jVLEsyInCE21uAbaepbbz/Rqfs/j+6a4bhMrEzzUAAR1kAn1Aq2+Hw5CtcveIRGSII0MzI56bcquYHGYbvWUWLcFSTddu8PIDRlAX3ba0uLrJSd77Ll0KYPDScU1bd8+pvOD2xdtummYaqfX+f30KdNdDUXZrGKuVlMDXNHOSST7zJiiWMRQ7REN4vSf51JPNFMZpxk0D2XSmNb50V4bhVZ4bURPr6kVZxlqxnNsobZ0hweo6Hl50culwOWtjNva0quyGjfEeHNZIJhlJ9J5weYonc4PavWw9oZCRpqSPRpPXSRQUGwuaRjmzfab401FrVcO4XbYNbuIVuLzk6g+yw1g9KGYDBoLxtXgd8oIMeLl7j+VdlOzA9VqRVq/xrhwsuCs5G28jzE/OmcOa1MXQ0HZlO3qKGXWwc2lysbfOnW7hAiaIYvhZUZ0bOh2I/H9fCr2D4KlxFfM0ka7b8+VdkYMyGXOO3TtlHun76qXuIXW3uN7jH3UqVO5MVJFG9iskZhmVyVcHWVgkj10rKX7Qt3bh5Fony1hveCD60qVWw/af4fsRxHYX5XuR8NhgzbzfnRSRC91l15wARRkXAZgg0qVKOj0Ka8YAanYdelKlXHFb/aFj/m2/4h+deri7bEFbiGN4I5xFKlV6C+7wfsZ8Q/t8V7l21iVU+IjzA1MegoN2Yxz277BSM3eW2TNzOtskx1V9YpUqg9jQtztI1qriMbbtGHaJ1GhMj3ClSp2IjMcX7ljmtOdTqkGB5ifuqgqeVKlWdl0SqtOTzpUq44mwt6LinowPzFXO1n9YpB+p+LUqVMuyxX2kAHcjnQTtDifCmbbON/QilSpY7jS2AXGEzWXcn7A/81ygmGxLroGaCIOtKlW2r2n4exhpdlePuT2sBdKhltXCDMMFYg7zBA8j86JcGsEosqSubWATInWlSqfeWcdjZxhdIWBO3dP/AJffWT4/gQ1/6G2RbOTXKVEwJ0I6zSpVKhh1GWjZerJuOpQ46oZlKL4AukDSAW/ATQ+27REmKVKtVfteCMNB/b4v3N32QUCwDO/4M35ittfHfWkc6EaEga8geYHQ++lSrHzZt5IpAtZubEMp+Pu8xRDiV1L4DJGfQQTBPlERM7a0qVAL3LWBtm7ZNu4rAjQEg8tjPUVR4Dj+7c22IysYGumbbTyP5UqVNtYXdMJY7FrbZe8WAfZub+oMTH3HTpQ/tPgsyi6vtKPFHMcj7vu9KVKmezAuRJgrgxWHKMfpF+/XK3odj76Ajhd+f6p/hNKlS2uFMksYi7Yb6w5lWGh9341qOG8StukkBDJkab7z86VKhF2HlFM//9k="
# #                         alt="camera" class="thumbnail">
# #                     <div class="caption">
# #                         <h2>Easy OCR</h2>
# #                         <p>Easy-OCR is used to recognise the characters on a licence plate that have been detected, and
# #                             it returns the characters in the same order as before, but in text format. .</p>
# #                     </div>
# #                 </a>
# #             </div>
# #             <div class="item">
# #                 <a href="#">
# #                     <img src="data:image/png;base64,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"
# #                         alt="watch" class="thumbnail">
# #                     <div class="caption"> <!-- comment -->
# #                         <h2>StreamLit</h2>
# #                         <p>Streamlit is an open-source app framework for Machine Learning and Data Science teams. Apart
# #                             from this it is used to create beautiful web apps and various other functionalities.</p>
# #                     </div>
# #                 </a>
# #             </div>
# #             <!--                 <div class="item">
# #                 <a href="#" >
# #                     <img src="https://sayantan-world.github.io/Internshala-ecommerce/img/shirt.jpg" alt="shirt" class="thumbnail"> -->
# #             <!--                     <div class="caption">
# #                         <h2></h2>
# #                         <p>Our exquisite collection of shirts.</p>
# #                     </div>
# #                 </a>
# #                 </div>
# #             </div>-->
# #         </div>
# #         <div class="footer">
# #             <div class="container">
# #                 <center>
# #                     Copyright @ Celestial Biscuit 26
# #                 </center>
# #             </div>
# #         </div>
# # </body><!-- comment -->

# # </html>""")
