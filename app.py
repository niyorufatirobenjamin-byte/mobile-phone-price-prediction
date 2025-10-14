# -*- coding: utf-8 -*-

import numpy as np
import pickle
import pandas as pd
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('phone_sales_data.sav', 'rb'))

# Function to make prediction
def phone_price_prediction(Brand, Battery_capacity_mAh, Screen_size_inches,
                            Touchscreen, Processor, RAM_MB, Internal_storage_GB,
                            Rear_camera, Operating_system, Number_of_SIMs,
                            three_G, four_G_LTE):
    # Create DataFrame from input
   new_phone = pd.DataFrame([{
    'Brand': 44,
    'Battery capacity (mAh)': 4085,
    'Screen size (inches)': 6.67,
    'Touchscreen': 1,
    'Processor': 8,
    'RAM (MB)': 12000,
    'Internal storage (GB)': 256.0,
    'Rear camera': 48.0,
    'Operating system': 0,
    'Number of SIMs': 2,
    '3G': 1,
    '4G/ LTE': 1
}])
    
    # Predict price
    predicted_price = loaded_model.predict(new_phone)
    return predicted_price[0]


# Streamlit app
def main():
    st.title("📱 Mobile Phone Price Prediction")

    # Input fields
    Brand = st.text_input('Brand (numeric code, e.g., 44)')
    Battery_capacity_mAh = st.text_input('Battery capacity (mAh) (e.g., 4085)')
    Screen_size_inches = st.text_input('Screen size (inches) (e.g., 6.67)')
    Touchscreen = st.text_input('Touchscreen (1 for Yes, 0 for No)')
    Processor = st.text_input('Processor (numeric code, e.g., 8)')
    RAM_MB = st.text_input('RAM (MB) (e.g., 12000)')
    Internal_storage_GB = st.text_input('Internal storage (GB) (e.g., 256)')
    Rear_camera = st.text_input('Rear camera (MP) (e.g., 48)')
    Operating_system = st.text_input('Operating system (numeric code, e.g., 0)')
    Number_of_SIMs = st.text_input('Number of SIMs (e.g., 2)')
    three_G = st.text_input('3G support (1 for Yes, 0 for No)')
    four_G_LTE = st.text_input('4G/LTE support (1 for Yes, 0 for No)')

    if st.button('Predict phone Price'):
        try:
            # Convert inputs
            Brand = int(Brand)
            Battery_capacity_mAh = int(Battery_capacity_mAh)
            Screen_size_inches = float(Screen_size_inches)
            Touchscreen = int(Touchscreen)
            Processor = int(Processor)
            RAM_MB = int(RAM_MB)
            Internal_storage_GB = float(Internal_storage_GB)
            Rear_camera = float(Rear_camera)
            Operating_system = int(Operating_system)
            Number_of_SIMs = int(Number_of_SIMs)
            three_G = int(three_G)
            four_G_LTE = int(four_G_LTE)

            # Predict
            price = phone_price_prediction(
                Brand, Battery_capacity_mAh, Screen_size_inches,
                Touchscreen, Processor, RAM_MB, Internal_storage_GB,
                Rear_camera, Operating_system, Number_of_SIMs,
                three_G, four_G_LTE
            )

            st.success(f'The predicted phone price is: RWF {price:.2f}')
        except ValueError:
            st.error("Please enter valid numeric values for all inputs.")


if __name__ == '__main__':
    main()


