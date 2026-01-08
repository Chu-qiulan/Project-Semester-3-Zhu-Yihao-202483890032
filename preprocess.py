import pandas as pd

data = pd.read_csv("data.csv")

window_size = 3
data["moisture_denoised"] = data["moisture"].rolling(
    window=window_size, min_periods=1
).mean()

min_val = data["moisture_denoised"].min()
max_val = data["moisture_denoised"].max()
data["moisture_norm"] = (data["moisture_denoised"] - min_val) / (max_val - min_val)

data.to_csv("processed_data.csv", index=False)

print("Data preprocessing completed successfully.")
