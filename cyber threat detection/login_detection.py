# login_detection.py

import pandas as pd
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
import os

# Create results folder if it doesn't exist
os.makedirs("results", exist_ok=True)

# Load simulated login data
df = pd.read_csv("simulated_login_data.csv")

# Use 'hour' and 'login_attempts' for anomaly detection
X = df[['hour', 'login_attempts']]

# One-Class SVM model
model = OneClassSVM(gamma='auto', nu=0.2)  # nu is sensitivity
model.fit(X)
df['anomaly'] = model.predict(X)  # -1 = anomaly

# Save results
df.to_csv("results/login_anomalies.csv", index=False)

# Plot
plt.figure(figsize=(10, 5))
plt.scatter(df['hour'], df['login_attempts'], c=df['anomaly'], cmap='coolwarm')
plt.title("Login Behavior Anomalies")
plt.xlabel("Login Hour")
plt.ylabel("Login Attempts")
plt.savefig("results/login_anomaly_plot.png")
plt.show()
