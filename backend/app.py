from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, UTC
import joblib
import pandas as pd
import os
import json
# from services.gemini_service import generate_recommendation
from services.ollama_service import generate_recommendation
from db.repository import save_prediction

app = Flask(__name__)
CORS(app)

# --- Load model + feature order once ---
model = joblib.load("models/depression_svm_x3_model.pkl")
feature_order = joblib.load("data/svm_feature_order.pkl")

LOG_PATH = "data/log.txt"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    

    # print("\n--- Incoming Request ---\n\n")
    # print(data)
    # print("\n\n------------------------\n")



    # --- Generate server timestamp ---
    date_time = datetime.now(UTC).isoformat()

    # --- Prepare features in correct order ---
    try:
        input_features = [data[f] for f in feature_order]
    except KeyError as e:
        return jsonify({"error": f"Missing feature: {str(e)}"}), 400

    df = pd.DataFrame([input_features], columns=feature_order)

    # --- Prediction ---
    prediction = model.predict(df)[0]
    confidence = model.predict_proba(df).max()

    print(f"Prediction: {prediction}, Confidence: {confidence:.4f}")

    tip = "Model confidence is low. Consider retaking the assessment."
    # if confidence < 0.6:
    #     tip = "Model confidence is low. Consider retaking the assessment."
    # else:
    #     tip = generate_recommendation(prediction, confidence, data)


    # --- Save to DB ---
    #save_prediction(data, date_time, int(prediction), float(confidence), tip)


    # # Append log entry
    # with open(LOG_PATH, "a", encoding="utf-8") as f:
    #     f.write(json.dumps({
    #         "timestamp": datetime.now().isoformat(),
    #         "request": data,
    #         "prediction": int(prediction),
    #         "confidence_score": float(confidence),
    #         "mental_health_tip": tip
    #     }) + "\n")


    return jsonify({
        "prediction": int(prediction),
        "confidence_score": float(confidence),
        "mental_health_tip": tip
    })


if __name__ == "__main__":
    app.run(debug=True)