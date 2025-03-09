# Knowledge Base
diseases = {
    "Flu": ["fever", "cough", "sore_throat", "runny_nose"],
    "Pneumonia": ["fever", "cough", "difficulty_breathing", "chest_pain"],
    "Diabetes": ["frequent_urination", "excessive_thirst", "fatigue", "blurred_vision"],
    "Hypertension": ["headache", "dizziness", "chest_pain", "shortness_of_breath"],
    "Arthritis": ["joint_pain", "stiffness", "swelling", "decreased_range_of_motion"],
    "HIV-AIDS": ["loss_of_weight", "swollen_glands","diarrhoea"]
}
def diagnose_disease(symptoms):
    possible_diseases = []
    for disease, disease_symptoms in diseases.items():
        if all(symptom in disease_symptoms for symptom in symptoms):
            possible_diseases.append(disease)
    return possible_diseases
def diagnose_disease(symptoms):
    possible_diseases = []
    for disease, disease_symptoms in diseases.items():
        if all(symptom in disease_symptoms for symptom in symptoms):
            possible_diseases.append(disease)
    return possible_diseases
def main():
    print("Welcome to the LingsMedic Healthcare Diagnosis System!")
    print("Please enter your symptoms separated by commas (e.g., fever, cough, sore_throat):")
    user_symptoms = input().lower().split(", ")
    possible_diagnoses = diagnose_disease(user_symptoms)
    if possible_diagnoses:
        print("Based on your symptoms, the possible diagnoses are:")
        for diagnosis in possible_diagnoses:
            print("- " + diagnosis)
    else:
        print("Sorry, we couldn't find a matching diagnosis based on your symptoms,contact your doctor.")


if __name__ == "__main__":
    main()