# DiabVoice – AI-Based Diabetes Diagnosis and Recommendation System

DiabVoice is an AI-powered diabetes prediction system that accepts health parameters through a frontend interface and returns personalized diabetes predictions along with medicine and diet suggestions using trained machine learning models.

---

FEATURES

- Diabetes prediction using trained ML models
- Personalized medicine and diet recommendations
- Supports both Basic and Advanced test types
- Flask backend with structured REST API
- Modular project structure with separate frontend and backend
- Input validation and error handling
- Two distinct recommendation models (basic & advanced)

---

PROJECT STRUCTURE

DiabVoice/
├── backend/                    # Flask API backend
│   ├── app.py                 # Flask application
│   ├── requirements.txt       # Backend dependencies
── ml_model/              # Trained model files (.pkl)
│    ├── model.pkl
│    ├── model_kaggle.pkl
│    ├── basic_med_diet_model.pkl
│    └── med_diet_model_2.pkl
│
├── frontend/                  # Frontend (HTML, JS or React)
│   ├── index.html             # Example HTML form
│   ├── style.css              # Styling (if used)
│   └── script.js              # JS to handle API requests
│
└── README.md                  # Project documentation

---

EXAMPLE API USAGE

Endpoint: POST /predict

Basic test input:
{
  "test_type": "basic",
  "Pregnancies": 2,
  "Glucose": 140,
  "BloodPressure": 75,
  "SkinThickness": 30,
  "Insulin": 100,
  "BMI": 32.0,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 45
}

Advanced test input:
{
  "test_type": "advanced",
  "gender": "female",
  "age": 50,
  "hypertension": 1,
  "heart_disease": 0,
  "bmi": 31.4,
  "HbA1c_level": 7.8,
  "blood_glucose_level": 180
}

Sample response:
{
  "prediction": "Diabetic",
  "medicine": ["Metformin"],
  "diet": ["Low-carb diet"]
}

---

HOW TO RUN

1. Clone the repository:
   git clone https://github.com/SanuHait/DiabPredict
   cd DiabVoice

2. Setup backend:
   cd backend
   pip install -r requirements.txt
   python app.py

   → Flask API runs at http://localhost:5000

3. Open frontend:
   Open `frontend/index.html` in a browser OR deploy it with a web server

---

REQUIREMENTS (Backend)

- Flask
- Flask-CORS
- scikit-learn
- pandas
- numpy

(Install using: `pip install -r requirements.txt`)

---

MACHINE LEARNING MODELS

Model Type           | File                             | Purpose
---------------------|----------------------------------|-------------------------------
Basic Diagnosis       model.pkl                          Predict diabetic or not
Advanced Diagnosis    model_kaggle.pkl                   Based on clinical test inputs
Med/Diet (Basic)      basic_med_diet_model.pkl           Recommend medicine & diet
Med/Diet (Advanced)   med_diet_model_2.pkl               Recommend medicine & diet

---

ACKNOWLEDGMENTS

- Datasets from public sources like Kaggle
- Developed by Sanu Hait as part of MCA final year project

---

CONTACT

Developer: Sanu Hait  
GitHub: https://github.com/SanuHait 
Email: sanuhait345@gmail.com
