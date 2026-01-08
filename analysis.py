import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("processed_data.csv")

print(data["moisture_norm"].describe())

plt.figure()
plt.plot(data["time"], data["moisture_norm"])
plt.xlabel("Time")
plt.ylabel("Normalized Soil Moisture")
plt.title("Soil Moisture Trend Over Time")
plt.show()
