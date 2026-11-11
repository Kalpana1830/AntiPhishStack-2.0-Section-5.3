"""Flask API snippet reconstructed from report section 5.3."""

from catboost import CatBoostClassifier
from flask import Flask, jsonify, request

from scripts.feature_engineering import extract_features

app = Flask(__name__)
model = CatBoostClassifier()
model.load_model("models/catboost_model.cbm")


@app.route("/predict", methods=["POST"])
def predict():
    url = request.json["url"]
    features = extract_features(url)
    prediction = model.predict([features])
    label = "Phishing" if prediction[0] == 1 else "Benign"
    return jsonify({"url": url, "prediction": label})


if __name__ == "__main__":
    # Retained from the report snippet; debug mode is not suitable for production.
    app.run(debug=True)
