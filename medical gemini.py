class DiseaseDiagnosisSystem:
    def __init__(self):
        self.knowledge_base = {
            "Influenza": {
                "symptoms": ["fever", "cough", "sore throat", "body aches", "fatigue"],
                "probability": 0.8,
            },
            "Common Cold": {
                "symptoms": ["runny nose", "sneezing", "sore throat", "cough"],
                "probability": 0.7,
            },
            "Pneumonia": {
                "symptoms": ["cough", "fever", "chest pain", "shortness of breath", "fatigue"],
                "probability": 0.9,
            },
            "Malaria": {
                "symptoms": ["fever", "chills", "sweats", "headache", "muscle aches"],
                "probability": 0.85,
            },
            "Typhoid": {
                "symptoms": ["high fever", "headache", "abdominal pain", "weakness", "rash"],
                "probability": 0.75,
            },
        }

    def diagnose(self, symptoms):
        """Diagnoses a disease based on the given symptoms."""
        possible_diagnoses = {}
        for disease, data in self.knowledge_base.items():
            matched_symptoms = set(symptoms).intersection(data["symptoms"])
            match_percentage = len(matched_symptoms) / len(data["symptoms"]) if len(data["symptoms"]) > 0 else 0
            if match_percentage > 0.5:  # Consider a match if at least 50% of symptoms match
                possible_diagnoses[disease] = match_percentage * data["probability"]

        if possible_diagnoses:
            sorted_diagnoses = sorted(possible_diagnoses.items(), key=lambda item: item[1], reverse=True)
            return sorted_diagnoses
        else:
            return None

    def get_user_input(self):
        """Gets symptom input from the user."""
        print("Enter your symptoms (separated by commas):")
        symptoms_input = input().lower()
        symptoms = [s.strip() for s in symptoms_input.split(",")]
        return symptoms

    def run(self)
        symptoms = self.get_user_input()
        diagnosis = self.diagnose(symptoms)

        if diagnosis:
            print("\nPossible Diagnoses:")
            for disease, probability in diagnosis:
                print(f"- {disease}: (Probability: {probability:.2f})")
        else:
            print("\nNo matching diagnosis found.")