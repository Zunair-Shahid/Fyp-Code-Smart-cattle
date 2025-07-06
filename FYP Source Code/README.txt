
How to Run the Flask ML API with Ngrok

1. Install dependencies:
   pip install flask numpy scikit-learn

2. Run the app:
   python app.py

3. Install ngrok from: https://ngrok.com/

4. Start ngrok:
   ngrok http 5000

5. Use the public URL from ngrok to send POST requests:
   Example JSON:
   {
     "X": 0.2,
     "Y": 0.4,
     "Z": 0.6,
     "Temperature": 38.6,
     "Heartbeat": 75
   }

6. The response will be:
   { "prediction": "Healthy" }
