import joblib
import pandas as pd

# Load models
ammonia_model = joblib.load(
    "backend/ammonia_model.pkl"
)

fluoride_model = joblib.load(
    "backend/fluoride_model.pkl"
)

scaler = joblib.load(
    "backend/scaler.pkl"
)

feature_cols = [
    "pH",
    "Nitrate",
    "Nitrite-N (mg/L)",
    "COD (mg/L)",
    "DO (mg/L)",
    "TDS (mg/L)",
    "Turbidity (NTU)"
]


def prepare_input(
    ph,
    nitrate,
    nitrite,
    cod,
    do,
    tds,
    turbidity
):

    return pd.DataFrame(
        [[
            ph,
            nitrate,
            nitrite,
            cod,
            do,
            tds,
            turbidity
        ]],
        columns=feature_cols
    )


def prepare_scaled_input(*values):
    data = prepare_input(*values)
    return scaler.transform(data)

# Ammonia prediction
def predict_ammonia(
    ph,
    nitrate,
    nitrite,
    cod,
    do,
    tds,
    turbidity
):

    data = prepare_input(
        ph,
        nitrate,
        nitrite,
        cod,
        do,
        tds,
        turbidity
    )

    prediction = ammonia_model.predict(data)

    return round(float(prediction[0]), 3)

# Fluoride prediction
def predict_fluoride(
    ph,
    nitrate,
    nitrite,
    cod,
    do,
    tds,
    turbidity
):

    data = prepare_scaled_input(
        ph,
        nitrate,
        nitrite,
        cod,
        do,
        tds,
        turbidity
    )

    prediction = fluoride_model.predict(data)

    return round(float(prediction[0]), 3)
