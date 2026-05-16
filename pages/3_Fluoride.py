import streamlit as st

from backend.predict import (
    predict_fluoride
)

st.title("Fluoride Prediction")

ph = st.number_input("pH")

nitrate = st.number_input("Nitrate")

nitrite = st.number_input(
    "Nitrite-N (mg/L)"
)

cod = st.number_input("COD (mg/L)")

do = st.number_input("DO (mg/L)")

tds = st.number_input("TDS (mg/L)")

turbidity = st.number_input(
    "Turbidity (NTU)"
)

if st.button("Predict Fluoride"):

    prediction = predict_fluoride(
        ph,
        nitrate,
        nitrite,
        cod,
        do,
        tds,
        turbidity
    )

    st.success(
        f"Predicted Fluoride: {prediction} mg/L"
    )

    if (prediction > 1.5
        or tds > 1500
        or turbidity > 10
        or nitrate > 45
        or do < 3
        or cod > 50):
        st.error(
            "Unsafe Fluoride Level"
        )
    else:
        st.info(
            "Safe Fluoride Level"
        )