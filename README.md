# Cyber-Threat-Detection-Using-Python

Detecting Anomalies in Network Traffic, Login Behavior, and Phishing Websites

📚 Project Overview
This project focuses on basic cyber threat detection techniques using Python. It covers three key areas:

Network Traffic Anomaly Detection using packet analysis

Login Behavior Anomaly Detection based on time and frequency patterns

Phishing Website Detection using Machine Learning (Random Forest)

It is built to provide simple, understandable methods for detecting suspicious behavior in a system, serving as a basic educational model for anomaly detection in cybersecurity.

🛠️ Technologies Used
Python (Core Programming)

Pandas (Data handling)

Matplotlib (Data visualization)

Scikit-learn (Machine Learning)

Wireshark (Network packet capture for sample data)


⚡ Project Details
**1. Network Traffic Anomaly Detection**
Analyzes packet lengths from network traffic logs.

Flags packets as anomalies if size exceeds a threshold.

Visualization: Blue plot for normal, Red markers for anomalies.

2. **Login Behavior Anomaly Detection**
Analyzes login attempts by users.

Detects anomalies based on irregular login times or frequency.

Visualization: Scatter plot showing normal vs. anomalous login attempts.

**3. Phishing Website Detection**
Classifies websites into legitimate or phishing based on attributes like URL length, SSL presence, and suspicious symbols.

Achieved 100% accuracy on sample test data using Random Forest Classifier.

🧪 How to Run
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
Run each detection script:

bash
Copy
Edit
python network_detection.py
python login_behavior.py
python phishing_detection.py
Outputs will be saved in the /results folder, and visualizations will be shown.

📈 Sample Outputs
Network anomaly detection graph

Login anomaly scatter plot

Phishing detection classification report

🚀 Future Enhancements
Real-time monitoring using live network capture.

Integration with alert systems (email, SMS).

Use of Deep Learning models for phishing detection.

🧑‍💻 Author
Vivek NAth
B.Tech Student | AI & ML Enthusiast | Cybersecurity Learner

✅ This project is designed for educational purposes to build foundational understanding of anomaly detection techniques in cybersecurity.
