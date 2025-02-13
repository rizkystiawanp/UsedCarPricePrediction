import streamlit as st
import eda
import predict

with st.sidebar:
    st.title('Navigation')
    Navigation = st.selectbox('Page',['EDA','Predict Price'])

    st.write('___')
    st.write('About')


if Navigation == 'EDA':
    eda.run()
else:
    predict.run()