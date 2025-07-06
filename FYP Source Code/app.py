
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("cattle_health_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
    return "Cattle Health Prediction API is running."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array([[
            data["X"], data["Y"], data["Z"],
            data["Temperature"], data["Heartbeat"]
        ]])
        prediction = model.predict(features)[0]
        result = "Healthy" if prediction == 1 else "Unhealthy"
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
