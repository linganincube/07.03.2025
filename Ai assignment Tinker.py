import tkinter as tk
from tkinter import ttk, messagebox


class MedicalExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Lings Medical Diagnosis Assistant")
        self.root.geometry("1000x700")

        # Structured knowledge base
        self.knowledge_base = {
            "Influenza (Flu)": {
                "symptoms": {
                    "Fever": 0.9,
                    "Cough": 0.8,
                    "Sore throat": 0.7,
                    "Muscle aches": 0.6,
                    "Headache": 0.5
                },
                "info": "Viral infection affecting respiratory system"
            },
            "Malaria": {
                "symptoms": {
                    "High fever": 1.0,
                    "Chills": 0.9,
                    "Sweating": 0.8,
                    "Headache": 0.6,
                    "Nausea": 0.5
                },
                "info": "Mosquito-borne infectious disease"
            },
            "Typhoid": {
                "symptoms": {
                    "Prolonged fever": 1.0,
                    "Abdominal pain": 0.8,
                    "Constipation": 0.6,
                    "Headache": 0.5,
                    "Loss of appetite": 0.4
                },
                "info": "Bacterial infection from contaminated food/water"
            },
            "Gastroenteritis": {
                "symptoms": {
                    "Diarrhea": 0.9,
                    "Vomiting": 0.8,
                    "Abdominal cramps": 0.7,
                    "Nausea": 0.6,
                    "Fever": 0.4
                },
                "info": "Intestinal infection causing stomach inflammation"
            },
            "Pneumonia": {
                "symptoms": {
                    "Chest pain": 0.9,
                    "Cough with phlegm": 0.8,
                    "Fever": 0.7,
                    "Shortness of breath": 0.7,
                    "Fatigue": 0.5
                },
                "info": "Lung infection causing air sac inflammation"
            }
        }

        # GUI components
        self.create_widgets()
        self.load_symptoms()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Symptom selection panel
        input_frame = ttk.LabelFrame(main_frame, text="Select Symptoms")
        input_frame.pack(fill=tk.X, pady=5)

        self.symptom_list = tk.Listbox(input_frame, selectmode=tk.MULTIPLE, height=10)
        scrollbar = ttk.Scrollbar(input_frame, orient=tk.VERTICAL, command=self.symptom_list.yview)
        self.symptom_list.configure(yscrollcommand=scrollbar.set)
        self.symptom_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Action buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)

        ttk.Button(button_frame, text="Diagnose", command=self.run_diagnosis).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_selections).pack(side=tk.LEFT, padx=5)

        # Results display
        result_frame = ttk.LabelFrame(main_frame, text="Diagnosis Results")
        result_frame.pack(fill=tk.BOTH, expand=True)

        self.result_text = tk.Text(result_frame, wrap=tk.WORD, state=tk.DISABLED)
        scroll_text = ttk.Scrollbar(result_frame, command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=scroll_text.set)

        scroll_text.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.pack(fill=tk.BOTH, expand=True)

    def load_symptoms(self):
        # Extract all unique symptoms from knowledge base
        symptoms = set()
        for disease in self.knowledge_base.values():
            symptoms.update(disease["symptoms"].keys())
        for symptom in sorted(symptoms):
            self.symptom_list.insert(tk.END, symptom)

    def run_diagnosis(self):
        selected = self.symptom_list.curselection()
        if not selected:
            messagebox.showwarning("Input Error", "Please select at least one symptom")
            return

        symptoms = [self.symptom_list.get(i) for i in selected]
        diagnosis = self.calculate_probabilities(symptoms)
        self.display_results(diagnosis, symptoms)

    def calculate_probabilities(self, symptoms):
        scores = {}
        for disease, data in self.knowledge_base.items():
            total_weight = sum(data["symptoms"].values())
            matched_weight = sum(weight for symptom, weight in data["symptoms"].items()
                                 if symptom in symptoms)
            scores[disease] = (matched_weight / total_weight) * 100

        return sorted(scores.items(), key=lambda x: x[1], reverse=True)

    def display_results(self, diagnosis, symptoms):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)

        self.result_text.insert(tk.END, "Selected Symptoms:\n- " + "\n- ".join(symptoms) + "\n\n")
        self.result_text.insert(tk.END, "Possible Diagnoses:\n\n")

        for disease, score in diagnosis:
            self.result_text.insert(tk.END,
                                    f"► {disease} ({score:.1f}% match)\n{self.knowledge_base[disease]['info']}\n\n")

        top_diagnosis = diagnosis[0]
        if top_diagnosis[1] > 60:
            self.result_text.insert(tk.END,
                                    f"\nMost Likely Diagnosis: {top_diagnosis[0]} ({top_diagnosis[1]:.1f}% match)")
        else:
            self.result_text.insert(tk.END,
                                    "\nNote: If no clear diagnosis is  found please consult a healthcare professional.")

        self.result_text.config(state=tk.DISABLED)

    def clear_selections(self):
        self.symptom_list.selection_clear(0, tk.END)
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalExpertSystem(root)
    root.mainloop()