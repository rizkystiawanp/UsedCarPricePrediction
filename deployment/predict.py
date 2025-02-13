# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib

def run():
    # load model
    with open('final_model_pipeline.pkl', 'rb') as file:
        model = joblib.load(file)

    # judul
    st.title('Prediksi Harga Mobil Bekas')

    # Create form for input data
    with st.form("my_form"):
        fueltype = st.selectbox('Fuel Type', ['Gas', 'Diesel'], placeholder='Input')
        aspiration = st.selectbox('Aspiration', ['Std', 'Turbo'], placeholder='Input')
        doornumber = st.selectbox('Number of Doors', ['Two', 'Four'], placeholder='Input')
        carbody = st.selectbox('Car Type', ['Sedan', 'Hatchback', 'Wagon', 'Convertible', 'Hardtop'], placeholder='Input')
        drivewheel = st.selectbox('Drive Wheel', ['Fwd', 'Rwd', '4wd'], placeholder='Input')
        enginelocation = st.selectbox('Engine Location', ['Front', 'Rear'], placeholder='Input')
        enginetype = st.selectbox('Engine Type', ['Ohc', 'L', 'Rotary', 'DoHC'], placeholder='Input')
        cylindernumber = st.selectbox('Number of Cylinders', ['Two', 'Three', 'Four', 'Five', 'Six', 'Eight'], placeholder='Input')
        fuelsystem = st.selectbox('Fuel System', ['Mpfi', '2bbl', '4bbl', 'idi', 'spdi'], placeholder='Input')
        
        # Default values for numeric inputs
        wheelbase = st.number_input('Wheelbase', min_value=80.0, max_value=120.0, step=0.1)
        carlength = st.number_input('Car Length (inches)', min_value=150.0, max_value=200.0, step=0.1)
        carwidth = st.number_input('Car Width (inches)', min_value=60.0, max_value=80.0, step=0.1)
        carheight = st.number_input('Car Height (inches)', min_value=50.0, max_value=70.0, step=0.1)
        curbweight = st.number_input('Empty Weight (lbs)', min_value=2000, max_value=5000, step=1)
        enginesize = st.number_input('Engine Capacity (cc)', min_value=50, max_value=5000, step=10)
        boreratio = st.number_input('Bore Ratio', min_value=2.0, max_value=5.0, value=3.43, step=0.01)
        stroke = st.number_input('Stroke', min_value=2.0, max_value=4.0, step=0.01)
        compressionratio = st.number_input('Compression Ratio', min_value=5.0, max_value=15.0, step=0.1)
        horsepower = st.number_input('Horsepower', min_value=50, max_value=500, step=5)
        peakrpm = st.number_input('Peak RPM', min_value=1000, max_value=10000, step=100)
        citympg = st.number_input('City MPG', min_value=5, max_value=100, step=1)
        highwaympg = st.number_input('Highway MPG', min_value=5, max_value=100, step=1)

        # Submit button
        submitted = st.form_submit_button("Submit")

    # Collect input data when form is submitted
    if submitted:
        st.write('Data Input Results')
        input_data = pd.DataFrame({
            'fueltype': [fueltype],
            'aspiration': [aspiration],
            'doornumber': [doornumber],
            'carbody': [carbody],
            'drivewheel': [drivewheel],
            'enginelocation': [enginelocation],
            'enginetype': [enginetype],
            'cylindernumber': [cylindernumber],
            'fuelsystem': [fuelsystem],
            'wheelbase': [wheelbase],
            'carlength': [carlength],
            'carwidth': [carwidth],
            'carheight': [carheight],
            'curbweight': [curbweight],
            'enginesize': [enginesize],
            'boreratio': [boreratio],
            'stroke': [stroke],
            'compressionratio': [compressionratio],
            'horsepower': [horsepower],
            'peakrpm': [peakrpm],
            'citympg': [citympg],
            'highwaympg': [highwaympg]
    })

        st.dataframe(input_data, hide_index=True)

        # prediksi
        result = model.predict(input_data)

        # tampilkan hasil
        st.write(f'# Predicted Price:', round(result[0],ndigits=None))


    