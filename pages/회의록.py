import streamlit as st
import datetime
import pandas as pd
from st_aggrid import AgGrid

st.set_page_config(layout = "wide", initial_sidebar_state = "expanded")

날짜 = st.date_input("회의 일자",datetime.datetime.now())
회의참석자 = st.text_input("회의 참석자 명단")
회의내용 = st.text_area("회의 내용")

데이터취합 = [날짜,회의참석자,회의내용]

저장 = st.button('회의록 저장')

index = 0
if 저장:
    회의록저장 = pd.read_csv('./db/CSPI_EXPO_2023_회의록.csv',encoding='cp949')
    data_to_insert = {'회의일자': 날짜, '참석자명단': 회의참석자, '회의내용': 회의내용}
    df = 회의록저장.append(data_to_insert,ignore_index=True)
    df.to_csv('./db/CSPI_EXPO_2023_회의록.csv',encoding='cp949',index = False)

st.subheader('✒️회의록')

회의록내용 = pd.read_csv('./db/CSPI_EXPO_2023_회의록.csv',encoding='cp949')
AgGrid(회의록내용,allow_unsafe_jscode=True,theme='balham',columns_auto_size_mode=1)

