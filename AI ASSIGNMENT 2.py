import re

# Knowledge Base: FAQs and Answers
knowledge_base = {
    "admission requirements": "To apply, you need a high school diploma, transcripts, and a completed application form.",
    "application deadline": "The application deadline for the fall semester is August 1st.",
    "tuition fees": "Tuition fees vary by program. Please visit our website for detailed fee structures.",
    "scholarships": "We offer merit-based and need-based scholarships. Check the financial aid section on our website.",
    "course catalog": "You can find the course catalog on the university website under the 'Academics' section.",
    "student housing": "On-campus housing is available. Applications open in March for the next academic year.",
    "contact information": "You can contact the admissions office at admissions@cuz.ac.zw or call +263-868-800-2370.",
    "artificial intelligence lecturer":"Dr S Masimba",
    "best graduate":"Lingani Ncube",
    "how do i apply":"Please visit www.cuz.ac.zw and click on new application",
    "physical address of university": '18443, Cranborne Avenue, Hatfield, Harare'
}

# Preprocess text: Convert to lowercase and remove special characters
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

# Match user query to the knowledge base
def get_response(query):
    query = preprocess(query)
    for question, answer in knowledge_base.items():
        if query in question or any(word in query for word in question.split()):
            return answer
    return "I'm sorry, I don't have information on that. Please contact the university directly."

# Chatbot Interface
def chatbot():
    print("Welcome to the Catholic University of Zimbabwe Student Support Chatbot!")
    print("How can I assist you today? You can ask about admissions, scholarships, tuition, and more.")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye! Have a great day.")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Test the chatbot
if __name__ == "__main__":
    chatbot()