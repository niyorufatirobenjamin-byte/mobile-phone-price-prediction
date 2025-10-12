# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 10:14:20 2025

@author: Admin
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st


# Load the trained model
loaded_model = pickle.load(open('C:/Users/Benjamin/Desktop/mobile phone price prediction/phone prediction prices/phone_sales_data.sav', 'rb'))

# Main Streamlit app
def main():
    st.title("mobile phone Price Prediction")

    # Input fields for all features
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
        # Convert inputs to numeric types
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

        # Call the prediction function (just fix indentation)
         price = phone_sales_data(
            Brand, Battery_capacity_mAh, Screen_size_inches,
            Touchscreen, Processor, RAM_MB, Internal_storage_GB,
            Rear_camera, Operating_system, Number_of_SIMs,
            three_G, four_G_LTE
        )

         st.success(f'The predicted price for the switch is: RWF {price:.2f}')
        except ValueError:
            
         st.error("Please enter valid numeric values for all inputs.")
if __name__ == '__main__':
    main()         