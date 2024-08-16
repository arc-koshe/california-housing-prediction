# Col. names -> ['housing_median_age', 'total_rooms', 'population', 'median_income', 'ocean_proximity', 'rooms_per_house', 'bedrooms_ratio', 'people_per_house']

import pickle
import streamlit as st
import warnings
import pandas as pd
import numpy as np
warnings.filterwarnings("ignore")

# Load the model
with open('California_housing_regression.pkl', 'rb') as file:
    model_test = pickle.load(file)

def main():
    st.title("Housing Price Prediction")

    # User input fields with default values
    housing_median_age = st.slider("Housing Median Age", min_value=0, max_value=52)
    total_rooms = st.number_input("Total Rooms", value=1000, min_value=1)
    population = st.number_input("Population", value=1000, min_value=1)
    median_income = st.number_input("Median Income", value=30000, min_value=1000)
    ocean_proximity = st.selectbox("Ocean Proximity", options=["<1H OCEAN", "INLAND", "NEAR OCEAN", "ISLAND", "NEAR BAY"])
    rooms_per_house = st.number_input("Rooms per House", value=5.0, min_value=0.0)
    bedrooms_ratio = st.number_input("Bedrooms Ratio", value=0.2, min_value=0.0)
    people_per_house = st.number_input("People per House", value=3.0, min_value=0.0)

    # Create a DataFrame from the user input
    input_data = pd.DataFrame({
        'housing_median_age': [housing_median_age],
        'total_rooms': [total_rooms],
        'population': [population],
        'median_income': [median_income],
        'ocean_proximity': [ocean_proximity],
        'rooms_per_house': [rooms_per_house],
        'bedrooms_ratio': [bedrooms_ratio],
        'people_per_house': [people_per_house]
    })

    # Validate input to ensure there are no infinities or NaNs
    if not input_data.replace([np.inf, -np.inf], np.nan).dropna().empty:
        # Make prediction
        prediction = model_test.predict(input_data)
        st.write("Predicted Housing Price:", prediction[0])
    else:
        st.error("Input contains invalid values (Infinity or NaN). Please check your inputs.")

if __name__ == '__main__':
    main()


#print(model_test.predict([[5,12,45245,90000,'INLAND',5,3,6.3]]))