import streamlit as st

from backend.predict import (
    predict_ammonia
)

st.title("Ammonia Prediction")

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

if st.button("Predict Ammonia"):

    prediction = predict_ammonia(
        ph,
        nitrate,
        nitrite,
        cod,
        do,
        tds,
        turbidity
    )

    st.success(
        f"Predicted Ammonia: {prediction} mg/L"
    )

    # Main ammonia danger
    if prediction > 0.5:

        st.error(
            "Unsafe Ammonia Level Detected!"
        )

    # Other water quality risks
    elif (
        cod > 50
        or turbidity > 10
        or nitrate > 45
        or do < 3
        or tds > 1500
    ):

        st.warning(
            "Water Quality Risk Detected Based on Other Parameters"
        )

    # Safe water
    else:

        st.success(
            "Safe Water Quality"
        )