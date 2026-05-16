import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from catboost import CatBoostRegressor
from xgboost import XGBRegressor

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
DATA_PATH = ROOT_DIR / "data" / "preprocessed_water_quality_data.csv"

# Load dataset
df = pd.read_csv(
    DATA_PATH,
    low_memory=False
)

# Features
feature_cols = [
    'pH',
    'Nitrate',
    'Nitrite-N (mg/L)',
    'COD (mg/L)',
    'DO (mg/L)',
    'TDS (mg/L)',
    'Turbidity (NTU)'
]

# Targets
target_ammonia = 'Ammonia'
target_fluoride = 'Fluoride (mg/L)'

model_cols = feature_cols + [
    target_ammonia,
    target_fluoride
]


def clean_numeric_column(series):
    return pd.to_numeric(
        series
        .astype(str)
        .str.strip()
        .str.replace(",", "", regex=False)
        .str.replace(r"(?<=\d)\.\.+(?=\d)", ".", regex=True)
        .str.extract(r"([-+]?\d*\.?\d+)", expand=False),
        errors="coerce"
    )


for col in model_cols:
    df[col] = clean_numeric_column(
        df[col]
    )

# Fill missing feature values and remove rows with missing targets
df[feature_cols] = df[feature_cols].fillna(
    df[feature_cols].median()
)

df = df.dropna(
    subset=[
        target_ammonia,
        target_fluoride
    ]
)

# Input features
X = df[feature_cols]

# Targets
y_ammonia = df[target_ammonia]

y_fluoride = df[target_fluoride]

# Scaling
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# Train test split
X_train_A, X_test_A, y_train_A, y_test_A = train_test_split(
    X,
    y_ammonia,
    test_size=0.2,
    random_state=42
)

X_train_F, X_test_F, y_train_F, y_test_F = train_test_split(
    X_scaled,
    y_fluoride,
    test_size=0.2,
    random_state=42
)

# Ammonia Model
preprocessor = StandardScaler()

ammonia_model = Pipeline(steps=[
    (
        "preprocessor",
        preprocessor
    ),
    (
        "model",
        XGBRegressor(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=6,
            subsample=0.8,
            colsample_bytree=0.8,
            objective="reg:squarederror",
            random_state=42
        )
    )
])

ammonia_model.fit(
    X_train_A,
    y_train_A
)

# Fluoride Model
fluoride_model = CatBoostRegressor(
    iterations=200,
    learning_rate=0.05,
    depth=6,
    verbose=0
)

fluoride_model.fit(
    X_train_F,
    y_train_F
)

# Save models
joblib.dump(
    ammonia_model,
    BASE_DIR / "ammonia_model.pkl"
)

joblib.dump(
    fluoride_model,
    BASE_DIR / "fluoride_model.pkl"
)

joblib.dump(
    scaler,
    BASE_DIR / "scaler.pkl"
)

print("Models Saved Successfully")
