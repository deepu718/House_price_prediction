import streamlit as st
import util

st.title("Banglore House Price Prediction :house:")

util.load_saved_artifacts()

loc,area = st.columns(2)

location = loc.selectbox("Location",util.get_location_names())

area_sq_ft = area.number_input("Area",min_value=700,max_value=15000,value=1000,step=5)

bhk,bath,balcony = st.columns(3)

bhk = bhk.slider("BHK",min_value=1,max_value=5,value=2,step=1)

bath = bath.slider("Bathrooms",min_value=1,max_value=5,value=2,step=1)

balcony = balcony.slider("Balcony",min_value=1,max_value=5,value=1,step=1)

if st.button("Predict"):
    price = util.get_estimated_price(location,area_sq_ft,bhk,bath,balcony)
    st.write(f"Predicted Price of the house is {price} lakhs")
