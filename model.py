import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("processed_data.csv")

X = data[["time"]]
y = data["moisture_norm"]

model = LinearRegression()
model.fit(X, y)

future_time = np.array([[16], [17], [18], [19], [20]])
future_prediction = model.predict(future_time)

plt.figure()
plt.plot(data["time"], y, label="Actual")
plt.plot(future_time.flatten(), future_prediction, label="Predicted")
plt.xlabel("Time")
plt.ylabel("Normalized Soil Moisture")
plt.title("Soil Moisture Prediction")
plt.legend()
plt.show()
