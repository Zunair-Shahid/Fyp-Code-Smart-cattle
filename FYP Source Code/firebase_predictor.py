import firebase_admin
from firebase_admin import credentials, db
import requests
import time


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://smart-cattle-database-default-rtdb.firebaseio.com/"
})


PREDICT_URL = "https://61e1-202-47-45-241.ngrok-free.app/predict"  


def get_prediction(sensor_data):
    try:
        response = requests.post(PREDICT_URL, json=sensor_data)
        return response.json().get("prediction", "Unknown")
    except Exception as e:
        print("Error calling model:", e)
        return "Error"


ref = db.reference("cattle/cow1")
last_data = None

print("Monitoring Firebase for cow1 sensor data...")

while True:
    data = ref.get()

    # Check for sensor data
    if data:
        sensor_data = {
            "X": data.get("accelX", 0),
            "Y": data.get("accelY", 0),
            "Z": data.get("accelZ", 0),
            "Temperature": data.get("temperature", 0),
            "Heartbeat": data.get("pulse", 0)
        }

        if sensor_data != last_data:
            last_data = sensor_data
            print("New Data:", sensor_data)

            prediction = get_prediction(sensor_data)
            print("Prediction:", prediction)

            # Update Firebase with prediction
            ref.update({"HealthStatus": prediction})

    time.sleep(2)
