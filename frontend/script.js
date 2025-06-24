const inputFields = document.getElementById("input-fields");
const testTypeSelect = document.getElementById("test-type");
const form = document.getElementById("diagnosis-form");

const fieldConfigs = {
  basic: [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
  ],
  advanced: [
    "age", "hypertension", "heart_disease", "bmi", 
    "HbA1c_level", "blood_glucose_level", "gender"
  ]
};

// Update form dynamically
function generateForm(type) {
  inputFields.innerHTML = "";
  fieldConfigs[type].forEach(field => {
    const label = document.createElement("label");
    label.innerText = field;
    const input = document.createElement("input");
    input.name = field;
    input.required = true;
    input.placeholder = field;
    inputFields.appendChild(label);
    inputFields.appendChild(input);
  });
}

// Initial form
generateForm(testTypeSelect.value);
testTypeSelect.addEventListener("change", () => generateForm(testTypeSelect.value));

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const test_type = testTypeSelect.value;
  const data = { test_type };

  for (let [key, value] of formData.entries()) {
    if (key !== "test-type") {
      data[key] = isNaN(value) ? value : parseFloat(value);
    }
  }

  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("prediction").innerText = result.prediction;
    document.getElementById("medicine").innerText = result.medicine.join(", ") || "None";
    document.getElementById("diet").innerText = result.diet.join(", ") || "None";

  } catch (error) {
    alert("Prediction failed. Check API or console.");
    console.error(error);
  }
});
