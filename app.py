import streamlit as st
import cv2
import numpy as np
import easyocr as ocr
import pandas as pd

df  = pd.read_csv('./db/CSPI_EXPO_2023.csv',encoding="cp949")
st.set_page_config(page_icon="🔆",layout = "wide", initial_sidebar_state = "expanded")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 1rem;
                    padding-left: 1rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)
st.sidebar.markdown('<h1><div style="text-align: left;">😃CSPI EXPO 2023 App</div></h1>', unsafe_allow_html=True)
st.sidebar.markdown('<h2><div style="text-align: left;">📅2023.05.24 ~ 2023.05.26</div></h2>', unsafe_allow_html=True)
st.sidebar.markdown('<h2><div style="text-align: left;"><a href = "https://cspi-expo.com/en/">CSPI EXPO 홈페이지</a></div></h2>', unsafe_allow_html=True)

map_data = pd.DataFrame({'lat' : [35.64836],'lon' : [140.03553]})
st.sidebar.map(map_data,zoom=11, use_container_width=True)

uploaded_file = st.file_uploader("Business Card")

col1, col2 = st.columns(2)
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    with col1:
        st.image(opencv_image,channels='BGR')
        langs = ['ko', 'en']
        reader = ocr.Reader(lang_list=langs, gpu=True)
        results = reader.readtext(opencv_image, detail=0)
    with col2:
        st.write(results)

edited_df = st.experimental_data_editor(df, num_rows="dynamic", width=1550, key="data_editor")

save_results = st.button('자료 저장')

if save_results:
    edited_df = edited_df.to_csv('./db/CSPI_EXPO_2023.csv',encoding="cp949", index=False)
