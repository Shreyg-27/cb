import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date
import cv2
from st_aggrid import AgGrid
from st_aggrid import GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from google.cloud import firestore
# from firebase_admin import auth
# from main import *

# user = auth.get_user_by_email(email)
# print('Successfully fetched user data: {0}'.format(user.uid))
st.header("Today's entries")
if 'count' not in st.session_state:
    st.session_state.count = 0

db = firestore.Client.from_service_account_json("firestore-key.json")


def sel():
    for row in selected_rows:
        nId = row['_selectedRowNodeInfo']['nodeId']
        doc_ref = db.collection("license").document(df.at[int(nId), 'Name'])
        doc_ref.set({'OutTime': firestore.SERVER_TIMESTAMP}, merge=True)
        df.at[nId, 'OutTime'] = doc_ref.get({'OutTime'})


today = datetime.datetime.combine(datetime.date.today(),
                                  datetime.time(00, 00, 00))

docs = db.collection('license').where(
    'userid', '==', 'abc').where('InTime', '>', today).stream()
df = pd.DataFrame(columns=['Name', 'Number',
                  'InTime', 'OutTime'])
for doc in docs:
    dict = doc.to_dict()
    Dict = {'Name': doc.id}
    Dict.update(dict)
    df = df.append(Dict, ignore_index=True)

gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_selection(selection_mode='single', use_checkbox=True)
gridoptions = gd.build()
grid_table = AgGrid(df, height=250, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

selected_rows = grid_table["selected_rows"]
st.button(label='Exited', on_click=sel())
