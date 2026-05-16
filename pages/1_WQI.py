import streamlit as st

from backend.wqi import (
    calculate_wqi,
    classify_wqi
)

st.title("WQI Prediction")

ph = st.number_input("pH")

nitrate = st.number_input("Nitrate")

do = st.number_input("DO (mg/L)")

tds = st.number_input("TDS (mg/L)")

turbidity = st.number_input(
    "Turbidity (NTU)"
)

ammonia = st.number_input("Ammonia")

fluoride = st.number_input(
    "Fluoride (mg/L)"
)

if st.button("Calculate WQI"):

    wqi = calculate_wqi(
        ph,
        nitrate,
        do,
        tds,
        turbidity,
        ammonia,
        fluoride
    )

    category = classify_wqi(wqi)

    st.success(f"WQI Value: {wqi}")

    st.info(f"WQI Category: {category}")