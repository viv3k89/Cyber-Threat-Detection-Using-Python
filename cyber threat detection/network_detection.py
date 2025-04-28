# network_detection.py

import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import os

# Create results directory if it doesn't exist
os.makedirs("results", exist_ok=True)

# Load Wireshark-exported CSV
df = pd.read_csv("cyber_threat_detectionwireshark_592_data.csv")

# Use only numerical features that make sense
# You can adjust these columns based on your CSV headers
features = ['No.', 'Time', 'Length']
df = df[features].dropna()

# Model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df[['Length']])
df['anomaly'] = model.predict(df[['Length']])  # -1 = anomaly

# Save results
df.to_csv("results/network_anomalies.csv", index=False)

# Print + Plot
print("=== Anomalies Found ===")
print(df[df['anomaly'] == -1])

# Optional: plot
plt.figure(figsize=(10, 4))
plt.plot(df['Length'], label='Packet Lengths')
plt.scatter(df.index[df['anomaly'] == -1], df['Length'][df['anomaly'] == -1], color='red', label='Anomaly')
plt.title("Network Anomaly Detection")
plt.xlabel("Packet Index")
plt.ylabel("Length")
plt.legend()
plt.savefig("results/network_anomaly_plot.png")
plt.show()

