# ♻️ SmartBin AI – AI-Powered Waste Classification System

**SmartBin AI** is an AI-powered web application developed using **Python (Flask)** and **Machine Learning** to classify waste into categories such as **Dry**, **Wet**, and **Plastic** based on sensor readings.

The system analyzes data collected from multiple sensors and predicts the waste type with a confidence score, helping improve waste segregation and support sustainable waste management.

---

## Features

* 🤖 AI-based Waste Classification
* 📊 Machine Learning Prediction Model
* 📈 Prediction Confidence Score
* 🌡️ Sensor-Based Waste Detection
* 💻 Responsive Web Interface
* ⚡ Fast and Accurate Predictions
* 🌱 Supports Smart Waste Management

---

##  Input Parameters

The model accepts the following sensor values:

* Moisture
* Infrared
* Capacitive
* Ultrasonic
* Temperature
* Optical
* Conductivity
* Weight

---

## Output

The system predicts one of the following waste categories:

* 🟢 Wet Waste
* 🔵 Dry Waste
* 🟡 Plastic Waste

Along with:

* Prediction Confidence (%)

---

## Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Dataset

* CSV Dataset (`waste_classification_data.csv`)

---

## 📁 Project Structure

```text
SmartBin-AI/
│
├── app.py
├── model.py
├── waste_classification_data.csv
├── README.md
├── Screenshot1.png
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    └── index.html
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Shrushti7823/SmartBin-AI.git
```

### Move into the Project Folder

```bash
cd SmartBin-AI
```

### Install Required Packages

```bash
pip install flask pandas numpy scikit-learn
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Project Screenshot

Add your application screenshot here.

Example:

```
Screenshot.png
```

---

## 🎯 Future Enhancements

* Image-Based Waste Detection
* MongoDB Database Integration
* User Authentication
* Prediction History
* Analytics Dashboard
* Recycling Recommendations
* Admin Panel
* Dark Mode
* Waste Statistics
* Mobile Responsive UI

---

## 📄 License

This project is developed for educational and academic purposes.

---

## Developer
**Shrushti R. Handge**

