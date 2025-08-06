import streamlit as st
import pickle
import json
import numpy as np

# Load the trained model and column information
with open('banglore_home_prices_model.pickle', 'rb') as f:
    __model = pickle.load(f)

with open('columns.json', 'r') as f:
    # Corrected this line to pass the file object 'f'
    __data_columns = json.load(f)['data_columns']
    __locations = sorted([col.replace('location_', '') for col in __data_columns if 'location_' in col])


def predict_price(location, sqft, bath, bhk):
    """
    Predicts the price of a house based on location, sqft, bath, and bhk.
    """
    try:
        # Find the index for the location column
        loc_index = __data_columns.index('location_' + location.lower())
    except ValueError:
        # If location is not found, it won't be one-hot encoded
        loc_index = -1

    # Create a numpy array with the correct number of features
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    # Predict the price and round it
    return round(__model.predict([x])[0], 2)

def main():
    """
    Main function to run the Streamlit app.
    """
    st.set_page_config(page_title="Bengaluru House Price Prediction", page_icon="🏡")
    st.title("Bengaluru House Price Prediction 🏡")

    st.write("Enter the details of the house to get an estimated price.")

    # Create a dropdown for location selection
    location = st.selectbox("Select Location", __locations)

    # Input fields for house features
    total_sqft = st.number_input("Total Square Feet", min_value=300, max_value=30000, value=1000, step=50)
    bath = st.number_input("Number of Bathrooms", min_value=1, max_value=20, value=2, step=1)
    bhk = st.number_input("Number of BHK", min_value=1, max_value=20, value=2, step=1)

    # Prediction button
    if st.button("Predict Price"):
        try:
            price = predict_price(location, total_sqft, bath, bhk)
            st.success(f"The estimated price is ₹ {price} Lakhs")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

if __name__ == '__main__':
    main()
