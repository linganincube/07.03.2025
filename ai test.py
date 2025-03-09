import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import random

# Download necessary NLTK resources (run once)
nltk.download('punkt')
nltk.download('wordnet')

class UniversityChatbot:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_input(self, user_input):
        """Tokenizes and lemmatizes the user's input."""
        tokens = word_tokenize(user_input.lower())
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        return lemmatized_tokens

    def find_best_match(self, user_input_tokens):
        """Finds the best matching question in the knowledge base."""
        best_match = None
        best_score = 0

        for question, response in self.knowledge_base.items():
            question_tokens = self.preprocess_input(question)
            score = len(set(user_input_tokens) & set(question_tokens))
            if score > best_score:
                best_score = score
                best_match = response

        return best_match

    def generate_response(self, user_input):
        """Generates a response based on the user's input."""
        user_tokens = self.preprocess_input(user_input)
        best_match = self.find_best_match(user_tokens)

        if best_match:
            return random.choice(best_match)
        else:
            return "I'm sorry, I don't understand. Could you please rephrase your question?"

    def run_chatbot(self):
        """Runs the chatbot in an interactive loop."""
        print("Welcome to the University Chatbot! How can I help you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Chatbot: Goodbye!")
                break
            response = self.generate_response(user_input)
            print("Chatbot:", response)

# Knowledge Base (Question-Response pairs)
knowledge_base = {
    "what are the admission requirements for computer science?": [
        "For Computer Science, you need a high school diploma with a minimum GPA of 3.5 and strong math skills.",
        "Admission to Computer Science requires a GPA of 3.5 or higher and a strong background in mathematics.",
        "To get into computer science, you'll need a GPA of at least 3.5 and solid math skills."
    ],
    "how do I apply for financial aid?": [
        "You can apply for financial aid by filling out the FAFSA form on our website.",
        "Financial aid applications are submitted through the FAFSA form, available on our university website.",
        "To apply for financial aid, please complete the FAFSA form found on the university's financial aid page."
    ],
    "where is the student services office?": [
        "The Student Services Office is located in the Student Union building, room 201.",
        "You can find the Student Services Office in room 201 of the Student Union building.",
        "Student Services is located in the Student Union building, room number 201."
    ],
    "what courses are offered in the business administration program?": [
        "The Business Administration program offers courses in accounting, marketing, finance, and management.",
        "Courses in the Business Administration program include accounting, marketing, finance, and management.",
        "Business Administration courses cover accounting, marketing, finance and management."
    ],
    "how do I register for classes?": [
        "You can register for classes through the student portal on our website.",
        "Class registration is done through the student portal on our university website.",
        "To register for classes, please use the student portal on the university's website."
    ],
    "what is the deadline for applications?": [
        "The deadline for applications is March 1st.",
        "Applications are due by March 1st.",
        "Please submit your applications before March 1st."
    ],
    "where is the library?": [
        "The library is located in the main building.",
        "You can find the library in the main building.",
        "The main building houses the university library."
    ],
    "what are the available scholarships?": [
        "Available scholarships include merit-based and need-based scholarships. Check our website for details.",
        "We offer merit and need based scholarships. Please visit our website for more information.",
        "Merit-based and need-based scholarships are available. Check our website for more details."
    ]
}

# Create and run the chatbot
chatbot = UniversityChatbot(knowledge_base)
chatbot.run_chatbot()
