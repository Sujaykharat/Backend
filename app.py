from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Health check route
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "✅ PaisaCheck3602 Scam Detection API is running!",
        "status": "active",
        "usage": {
            "POST /predict": "Send a JSON payload like {\"message\": \"text\"}"
        }
    })

# ✅ Prediction route (fixed typo here)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data.get('message', '')
    
    features = vectorizer.transform([message])
    prediction = model.predict(features)
    
    return jsonify({
        "message": message,
        "prediction": int(prediction[0]),
        "is_scam": bool(prediction[0])
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
