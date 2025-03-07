def __init__(self):
    self.knowledge_base = {
        'Common Cold': ['cough', 'sore throat', 'runny nose', 'sneezing', 'mild fever'],
        'Flu': ['fever', 'headache', 'muscle aches', 'fatigue', 'cough', 'sore throat'],
        'Malaria': ['high fever', 'chills', 'sweating', 'headache', 'nausea'],
        'Dengue': ['high fever', 'severe headache', 'pain behind eyes', 'joint pain', 'rash'],
        'Typhoid': ['prolonged fever', 'stomach pain', 'headache', 'loss of appetite', 'weakness']
    }
    self.all_symptoms = set(symptom for symptoms in self.knowledge_base.values() for symptom in symptoms)


def get_user_symptoms(self):
    print("Welcome to the Medical Diagnosis Expert System\n")
    print("Possible symptoms include:", ', '.join(sorted(self.all_symptoms)), "\n")
    user_input = input("Enter your symptoms separated by commas: ").strip().lower()
    return [symptom.strip() for symptom in user_input.split(',')]


def diagnose(self):
    user_symptoms = self.get_user_symptoms()
    scores = {disease: len(set(user_symptoms) & set(symptoms))
              for disease, symptoms in self.knowledge_base.items()}
    max_score = max(scores.values())
    possible_diseases = [disease for disease, score in scores.items() if score == max_score]

    print("\n--- Diagnosis Result ---")
    if max_score == 0:
        print("No specific diagnosis found. Please consult a healthcare professional.")
    else:
        print("Based on your symptoms, possible diagnosis:")
        for disease in possible_diseases:
            print(f"- {disease}")
        print("\nRecommended next steps: Consult a doctor for further evaluation and testing.")






