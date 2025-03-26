import streamlit as st
import pandas as pd
import numpy as np
import joblib

def run():
    # Title & Sub-header (centered)
    st.markdown(
        "<h1 style='text-align: center;'>🚗 Used Car Price Prediction</h1>", 
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center;'>Please enter vehicle details below to predict the selling price of the car.</p><hr>", 
        unsafe_allow_html=True
    )

    # Load model pipeline & features
    with open('final_model_pipeline.pkl', 'rb') as file:
        model = joblib.load(file)
    with open('selected_features.pkl', 'rb') as f:
        selected_features = joblib.load(f)

    # Layout tengah responsif
    left, center, right = st.columns([1, 2, 1])
    with center:
        with st.form("form_prediksi"):
            input_dict = {}

            for col in selected_features:
                if col == 'enginesize':
                    input_dict[col] = st.number_input(
                        'Engine Size', min_value=60, max_value=350, value=130, step=1,
                        help='Technical size of the engine (not in cc), represents engine power'
                    )
                elif col == 'curbweight':
                    input_dict[col] = st.number_input(
                        'Curb Weight', min_value=1500, max_value=4000, value=2500, step=10,
                        help='Weight of the car without passengers or cargo (in pounds)'
                    )
                elif col == 'horsepower':
                    input_dict[col] = st.number_input(
                        'Horsepower', min_value=50, max_value=300, value=110, step=1,
                        help='Engine power output (horsepower unit)'
                    )
                elif col == 'carwidth':
                    input_dict[col] = st.number_input(
                        'Car Width', min_value=60.0, max_value=75.0, value=65.0, step=0.1,
                        help='Overall width of the car (in inches)'
                    )
                elif col == 'highwaympg':
                    input_dict[col] = st.number_input(
                        'Highway MPG', min_value=15, max_value=60, value=30, step=1,
                        help='Fuel efficiency on highway driving (miles per gallon)'
                    )
                elif col == 'citympg':
                    input_dict[col] = st.number_input(
                        'City MPG', min_value=10, max_value=50, value=25, step=1,
                        help='Fuel efficiency in city driving (miles per gallon)'
                    )
                elif col == 'carlength':
                    input_dict[col] = st.number_input(
                        'Car Length', min_value=140.0, max_value=210.0, value=170.0, step=0.1,
                        help='Length of the car from front to back (in inches)'
                    )
                elif col == 'cylindernumber':
                    input_dict[col] = st.selectbox(
                        'Cylinder Number', ['Two', 'Three', 'Four', 'Five', 'Six', 'Eight', 'Twelve'],
                        help='Number of cylinders in the engine'
                    )
                elif col == 'fuelsystem':
                    input_dict[col] = st.selectbox(
                        'Fuel System', ['mpfi', '2bbl', '4bbl', 'idi', 'spdi'],
                        help='Fuel injection system used in the vehicle'
                    )
                elif col == 'drivewheel':
                    input_dict[col] = st.selectbox(
                        'Drive Wheel', ['fwd', 'rwd', '4wd'],
                        help='Type of drivetrain: front, rear, or 4-wheel drive'
                    )
                elif col == 'aspiration':
                    input_dict[col] = st.selectbox(
                        'Aspiration', ['std', 'turbo'],
                        help='Indicates whether the engine uses turbocharging'
                    )
                elif col == 'carbody':
                    input_dict[col] = st.selectbox(
                        'Car Body Type', ['sedan', 'hatchback', 'wagon', 'convertible', 'hardtop'],
                        help='General shape and design of the car body'
                    )

            submitted = st.form_submit_button("Predict")

        # Output prediction
        if submitted:
            input_df = pd.DataFrame([input_dict])
            st.write("📋 **Entered Data:**")
            st.dataframe(input_df)

            prediction = model.predict(input_df)[0]
            st.markdown(f"### 💰 Predicted Selling Price: **${round(prediction):,.2f}**")
