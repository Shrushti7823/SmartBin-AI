document
  .getElementById("sensorForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Collect sensor data from the form
    const moisture = document.getElementById("moisture").value;
    const infrared = document.getElementById("infrared").value;
    const capacitive = document.getElementById("capacitive").value;
    const ultrasonic = document.getElementById("ultrasonic").value;
    const temperature = document.getElementById("temperature").value;
    const optical = document.getElementById("optical").value;
    const conductivity = document.getElementById("conductivity").value;
    const weight = document.getElementById("weight").value;

    // Send data to the backend for prediction
    fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        moisture: moisture,
        infrared: infrared,
        capacitive: capacitive,
        ultrasonic: ultrasonic,
        temperature: temperature,
        optical: optical,
        conductivity: conductivity,
        weight: weight,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          alert("Error: " + data.error);
        } else {
          document.getElementById("wasteType").textContent = data.waste_type;
          document.getElementById("confidence").textContent = data.confidence;
        }
      })
      .catch((error) => console.error("Error:", error));
  });
