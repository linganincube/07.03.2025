import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report

# --- 1. Disease Dataset (Simplified) ---
# In a real application, this would be a much larger and more accurate dataset
data = {
    'Symptom': [
        "fever headache cough", "fever sore throat fatigue", "runny nose sneezing cough",
        "stomach pain vomiting diarrhea", "fatigue muscle aches headache",
        "fever chills body aches", "sore throat swollen glands", "nasal congestion postnasal drip",
        "abdominal cramps bloating gas", "nausea vomiting diarrhea",
        "high fever severe headache stiff neck", "persistent cough chest pain shortness of breath",
        "sore throat difficulty swallowing", "loss of appetite weight loss fatigue",
        "muscle weakness tingling numbness"
    ],
    'Disease': [
        "Flu", "Flu", "Common Cold",
        "Food Poisoning", "Flu",
        "Flu", "Strep Throat", "Common Cold",
        "Irritable Bowel Syndrome", "Food Poisoning",
        "Meningitis", "Pneumonia",
        "Strep Throat", "Anemia",
        "Multiple Sclerosis"
    ]
}
df = pd.DataFrame(data)

# --- 2. Machine Learning Model Training (Simplified) ---
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Symptom'])
y = df['Disease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

# --- 3. Disease Information (Simplified) ---
disease_info = {
    "Flu": "A common viral infection that can cause fever, cough, sore throat, and fatigue.",
    "Common Cold": "A mild viral infection of the nose and throat, often causing a runny nose, sneezing, and cough.",
    "Food Poisoning": "Illness caused by consuming contaminated food, leading to stomach pain, vomiting, and diarrhea.",
    "Strep Throat": "A bacterial infection of the throat, characterized by a sore throat and difficulty swallowing.",
    "Anemia": "A condition characterized by a deficiency of red blood cells or hemoglobin in the blood, resulting in fatigue and weakness.",
    "Meningitis": "Inflammation of the membranes surrounding the brain and spinal cord, often causing fever, headache, and stiff neck.",
    "Pneumonia": "Inflammation of the lungs, typically caused by an infection, leading to cough, chest pain, and shortness of breath.",
    "Irritable Bowel Syndrome": "A common condition that affects the digestive system, causing symptoms like abdominal cramps, bloating, and gas.",
    "Multiple Sclerosis": "A chronic disease that affects the central nervous system, leading to symptoms like muscle weakness and numbness."
}

# --- 4. GUI Functions ---
def predict_disease():
    symptoms = symptoms_entry.get()
    if not symptoms:
        messagebox.showerror("Error", "Please enter some symptoms.")
        return

    symptoms_vectorized = vectorizer.transform([symptoms])
    prediction = model.predict(symptoms_vectorized)[0]
    confidence = model.predict_proba(symptoms_vectorized).max() * 100  # Basic confidence

    result_label.config(text=f"Predicted Disease: {prediction} (Confidence: {confidence:.2f}%)")

    if prediction in disease_info:
        info_label.config(text=disease_info[prediction])
    else:
        info_label.config(text="No information available for this prediction.")

# --- 5. GUI Setup ---
window = tk.Tk()
window.title("Disease Diagnosis Bot")

symptoms_label = tk.Label(window, text="Enter Symptoms:")
symptoms_label.pack(pady=10)

symptoms_entry = tk.Entry(window, width=50)
symptoms_entry.pack(pady=5)

predict_button = tk.Button(window, text="Predict Disease", command=predict_disease)
predict_button.pack(pady=10)

result_label = tk.Label(window, text="Predicted Disease: ")
result_label.pack(pady=5)

info_label = tk.Label(window, text="")
info_label.pack(pady=5)

window.mainloop()