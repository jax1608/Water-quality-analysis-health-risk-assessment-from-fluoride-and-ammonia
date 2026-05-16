import streamlit as st

st.set_page_config(
    page_title="Water Quality Analysis",
    layout="wide"
)

st.title(
    "Water Quality Analysis & Health Risk Assessment"
)

st.markdown("""
## Features
- WQI Classification
- Ammonia Prediction
- Fluoride Prediction
- Health Risk Assessment
""")

st.sidebar.success(
    "Select a Page"
)