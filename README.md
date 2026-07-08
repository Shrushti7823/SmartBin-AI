# AI Waste Detection System

## Description

It is an online machine learning-based platform which accepts values of sensors and then predicts the waste type as dry, wet, or plastic.

## Screenshot

![Screenshot of the application](Screenshot%201.png)

## Features

- Accepts sensor values (Moisture, Infrared, Capacitive, Ultrasonic, Temperature, Optical, Conductivity, Weight)
- Predicts waste type: dry, wet, or plastic
- Displays prediction confidence
- User-friendly web interface

## Folder Structure

```
PBL TY AI Waste Detection/
  ├── app.py
  ├── model.py
  ├── README.md
  ├── Screenshot 1.png
  ├── static/
  │   ├── script.js
  │   └── style.css
  ├── templates/
  │   └── index.html
  └── waste_classification_data.csv
```

## How to Run the Project

1. Make sure you have Python installed.
2. In the root directory, run:
   ```bash
   python app.py
   ```
3. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Conclusion

This project demonstrates the use of machine learning for smart waste classification, helping to revolutionize waste management with AI technology.
