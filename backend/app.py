from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load diabetes prediction models
basic_model = pickle.load(open("D:/major project/DiabVoice/ml_model/model.pkl", "rb"))
advanced_model = pickle.load(open("D:/major project/DiabVoice/ml_model/model_kaggle.pkl", "rb"))

# Load new basic med/diet model
with open("D:/major project/DiabVoice/ml_model/basic_med_diet_model.pkl", "rb") as f:
    basic_bundle = pickle.load(f)

# Load advanced med/diet model
with open("D:/major project/DiabVoice/ml_model/med_diet_model_2.pkl", "rb") as f:
    advanced_bundle = pickle.load(f)

# ML-based Recommendation Logic
def get_recommendations(prediction, data, test_type):
    if prediction != "Diabetic":
        return {
            "prediction": prediction,
            "medicine": [],
            "diet": ["Balanced healthy diet with regular exercise"]
        }

    try:
        if test_type == "basic":
            features = [[
                float(data["Pregnancies"]),
                float(data["Glucose"]),
                float(data["BloodPressure"]),
                float(data["SkinThickness"]),
                float(data["Insulin"]),
                float(data["BMI"]),
                float(data["DiabetesPedigreeFunction"]),
                float(data["Age"])
            ]]
            bundle = basic_bundle

        elif test_type == "advanced":
            gender = data.get("gender", "Male")
            gender_encoded = 0 if gender.lower() == "male" else 1

            features = [[
                gender_encoded,
                float(data["age"]),
                int(data["hypertension"]),
                int(data["heart_disease"]),
                float(data["bmi"]),
                float(data["HbA1c_level"]),
                float(data["blood_glucose_level"])
            ]]
            bundle = advanced_bundle

        else:
            return {
                "prediction": prediction,
                "medicine": [],
                "diet": ["Invalid test_type provided."]
            }

        # Predict recommendations
        ml_meds = bundle["model_meds"].predict(features)[0]
        ml_diet = bundle["model_diet"].predict(features)[0]

        # Decode labels
        ml_med_label = bundle["label_encoder_meds"].inverse_transform([ml_meds])[0]
        ml_diet_label = bundle["label_encoder_diet"].inverse_transform([ml_diet])[0]

        return {
            "prediction": prediction,
            "medicine": [ml_med_label],
            "diet": [ml_diet_label]
        }

    except Exception as e:
        return {
            "prediction": prediction,
            "medicine": [],
            "diet": [f"Error in ML prediction: {str(e)}"]
        }

# Prediction API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    test_type = data.get("test_type", "basic")

    try:
        if test_type == "basic":
            features = [
                float(data["Pregnancies"]),
                float(data["Glucose"]),
                float(data["BloodPressure"]),
                float(data["SkinThickness"]),
                float(data["Insulin"]),
                float(data["BMI"]),
                float(data["DiabetesPedigreeFunction"]),
                float(data["Age"])
            ]
            model = basic_model

        elif test_type == "advanced":
            features = [
                float(data["age"]),
                float(data["hypertension"]),
                float(data["heart_disease"]),
                float(data["bmi"]),
                float(data["HbA1c_level"]),
                float(data["blood_glucose_level"])
            ]
            model = advanced_model

        else:
            return jsonify({"error": "Invalid test_type. Use 'basic' or 'advanced'."}), 400

        prediction = model.predict([features])[0]
        result = "Diabetic" if prediction == 1 else "Non-Diabetic"

        recommendation = get_recommendations(result, data, test_type)
        return jsonify(recommendation)

    except KeyError as e:
        return jsonify({"error": f"Missing or invalid input: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
