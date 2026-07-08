import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv('waste_classification_data.csv')

# Step 1: Data Preprocessing

# Splitting data into features (X) and target labels (y)
X = df.drop('Label', axis=1)  # Features: all columns except 'Label'
y = df['Label']  # Target: waste type (dry, wet, plastic)

# Encoding target labels to numerical values (as RandomForest needs numeric inputs)
le = LabelEncoder()
y_encoded = le.fit_transform(y)  # Convert 'dry', 'wet', 'plastic' to 0, 1, 2

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Scaling the features for better model performance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 2: Training RandomForest Classifier

# Create RandomForest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train_scaled, y_train)

def predict_waste_type(input_data):
    # Standardize the input data
    input_data_scaled = scaler.transform(input_data)

    # Predict the waste type and confidence
    prediction = rf_model.predict(input_data_scaled)
    prediction_proba = rf_model.predict_proba(input_data_scaled)

    # Convert prediction to label
    predicted_label = le.inverse_transform(prediction)[0]

    # Get the highest confidence score
    max_confidence = np.max(prediction_proba)

    return predicted_label, max_confidence
