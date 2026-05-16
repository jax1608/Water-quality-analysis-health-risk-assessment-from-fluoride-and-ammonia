import pandas as pd
import numpy as np

# Load combined dataset
df = pd.read_csv(
    "data/combined_water_quality.csv"
)

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing numeric values
numeric_cols = df.select_dtypes(
    include=np.number
).columns

for col in numeric_cols:

    df[col] = df[col].fillna(
        df[col].median()
    )

print("Missing Values Removed")

# Save final dataset
df.to_csv(
    "data/preprocessed_water_quality_data.csv",
    index=False
)

print("Preprocessed Dataset Saved")
print("Final Shape:", df.shape)