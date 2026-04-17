import os
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# 1. LOAD ASSETS (Ensure these 5 files are in your project folder)
try:
    model = joblib.load('mental_health_model.pkl')
    scaler = joblib.load('scaler.pkl')
    target_le = joblib.load('target_encoder.pkl')
    cat_encoders = joblib.load('categorical_encoders.pkl')
    feature_names = joblib.load('feature_names.pkl')
    print("🚀 All models and encoders loaded successfully!")
except Exception as e:
    print(f"❌ Error loading assets: {e}")

# 2. RISK MAPPING FOR USER CLARITY
RISK_INFO = {
    0: {
        "label": "Low Risk",
        "color": "Green",
        "advice": "You appear stable. Keep maintaining your current healthy habits!"
    },
    1: {
        "label": "Moderate Risk",
        "color": "Orange",
        "advice": "You might be stressed. Consider mindfulness and better sleep hygiene."
    },
    2: {
        "label": "High Risk",
        "color": "Red",
        "advice": "Significant risk detected. Please consult a mental health professional."
    }
}

@app.route('/', methods=['GET'])
def home():
    return "Mental Health Risk API is live and optimized!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        
        # 1. Convert categorical text to numbers safely
        for col, le in cat_encoders.items():
            if col in data:
                try:
                    data[col] = le.transform([str(data[col])])[0]
                except:
                    data[col] = 0 

        # 2. Safety Check: Ensure every feature the model needs is present
        final_features = []
        for name in feature_names:
            if name not in data:
                # If a name is missing, we default to 0 so the API doesn't crash
                final_features.append(0)
            else:
                final_features.append(data[name])
        
        # 3. Scale and Predict
        features_scaled = scaler.transform([final_features])
        prediction_idx = int(model.predict(features_scaled)[0])
        result = RISK_INFO.get(prediction_idx)

        return jsonify({
            'status': 'success',
            'prediction': {
                'score': prediction_idx,
                'risk_level': result['label'],
                'color_code': result['color'],
                'recommendation': result['advice']
            }
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)