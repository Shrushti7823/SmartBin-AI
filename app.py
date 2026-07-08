from flask import Flask, render_template, request
from model import predict_waste_type
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve data from the form
        moisture = float(request.form['moisture'])
        infrared = float(request.form['infrared'])
        capacitive = float(request.form['capacitive'])
        ultrasonic = float(request.form['ultrasonic'])
        temperature = float(request.form['temperature'])
        optical = float(request.form['optical'])
        conductivity = float(request.form['conductivity'])
        weight = float(request.form['weight'])

        # Prepare input data for prediction
        input_data = np.array([[moisture, infrared, capacitive, ultrasonic, temperature, optical, conductivity, weight]])
        
        # Predict waste type
        predicted_label, confidence = predict_waste_type(input_data)

        return render_template('index.html', prediction=predicted_label, confidence=confidence * 100)

    return render_template('index.html', prediction=None, confidence=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
