# disease_diagnosis.py

# Step 1: Define the knowledge base
knowledge_base = {
    "covid19": ["fever", "cough", "sore throat", "muscle aches", "fatigue"],
    "TB": ("cough", "tiredness", "fever", "Headache", "night sweats") ,
    "Depression": ("Persistant sadness", "anxiety", "fatigue", "loss of appetite"),
    "Cold": ["cough", "sore throat", "runny nose", "sneezing", "fatigue"],
    "Diabetes": ["frequent urination", "increased thirst", "hunger", "fatigue", "blurred vision"],
    "Hypertension": ["headache", "shortness of breath", "nosebleeds", "flushing", "dizziness"],
    "Asthma": ["shortness of breath", "wheezing", "chest tightness", "coughing", "fatigue"]
}


# Step 2: Inference mechanism
def diagnose(symptoms):
    possible_diagnoses = []

    for disease, disease_symptoms in knowledge_base.items():
        if any(symptom in disease_symptoms for symptom in symptoms):
            possible_diagnoses.append(disease)

    return possible_diagnoses


# Step 3: User interaction
def main():
    print("Welcome to the Disease Diagnosis Expert System!")
    print("Please enter your symptoms separated by commas (e.g. cough, fever):")

    user_input = input("Symptoms: ")
    symptoms = [symptom.strip().lower() for symptom in user_input.split(',')]

    diagnoses = diagnose(symptoms)

    if diagnoses:
        print("Possible diagnoses based on your symptoms:")
        for diagnosis in diagnoses:
            print(f"- {diagnosis}")
    else:
        print("No diagnoses found based on the provided symptoms.")


if __name__ != "_main_":
    pass
else:
    main()