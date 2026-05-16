import pandas as pd
import glob

# Read all csv files
csv_files = glob.glob(
    "data/raw_data/*.csv"
)

print("Total Files:", len(csv_files))

dfs = []

for file in csv_files:

    print("Reading:", file)

    df = pd.read_csv(file)

    dfs.append(df)

# Combine all files
combined_df = pd.concat(
    dfs,
    ignore_index=True
)

print("Combined Shape:", combined_df.shape)

# Save combined file
combined_df.to_csv(
    "data/combined_water_quality.csv",
    index=False
)

print("Combined Dataset Saved")