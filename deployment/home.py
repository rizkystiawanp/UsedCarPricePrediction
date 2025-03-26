import streamlit as st
from PIL import Image

def run():
    # Layout tiga kolom: kiri, tengah (konten), kanan
    left_col, center_col, right_col = st.columns([1, 2, 1])

    with center_col:
        # Judul dan deskripsi
        st.markdown("""
            <h1 style='text-align: center;'>🚗 Used Car Price Prediction</h1>
            <p style='text-align: center;'>Welcome! Estimate your car’s selling price easily.</p>
            <hr style="margin-top: 10px; margin-bottom: 25px;">
        """, unsafe_allow_html=True)

        # Tampilkan gambar dan resize dengan PIL
        image = Image.open("carpriced.jpg")
        resized_image = image.resize((700, 400))
        st.image(resized_image)

        # Konten penjelasan
        st.markdown("""
        <h4>🎯 Purpose of This App</h4>
        <p>This app helps users estimate the <b>selling price of used cars</b> using machine learning.</p>

        <h4>🛠️ How It Works</h4>
        <ol>
            <li><b>Input Car Specs</b> like engine size, horsepower, mpg, dimensions, etc.</li>
            <li>The input is processed using a <b>trained XGB Regressor model</b>.</li>
            <li>You will get an <b>instant prediction</b> of the car's estimated price.</li>
        </ol>

        <h4>📦 Tech Stack</h4>
        <ul>
            <li>Python + Streamlit</li>
            <li>Scikit-learn & XGBoost</li>
            <li>Pandas, NumPy, Joblib</li>
        </ul>

        <h4>🤝 Acknowledgement</h4>
        <p>Built for educational purpose to apply regression modeling in real-world context.</p>
        """, unsafe_allow_html=True)
