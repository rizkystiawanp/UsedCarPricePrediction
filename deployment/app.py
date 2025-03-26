# app.py
import streamlit as st
from streamlit_option_menu import option_menu
import home
import predict
import eda

# ⛳ Set konfigurasi halaman (harus paling atas)
st.set_page_config(page_title="Used Car Price App", layout="wide")

# 🔘 Navbar Horizontal
selected = option_menu(
    menu_title=None,
    options=["Home", "Predict Price", "EDA"],
    icons=["house", "car-front", "bar-chart"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f8f9fa"},
        "icon": {"color": "black", "font-size": "18px"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#ff4b4b", "color": "white"},
    }
)

# 📄 Render halaman sesuai pilihan
if selected == "Home":
    home.run()
elif selected == "Predict Price":
    predict.run()
elif selected == "EDA":
    eda.run()
