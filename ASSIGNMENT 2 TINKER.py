import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import scrolledtext

# Download NLTK resources (run once)
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

# Knowledge base (FAQ)
knowledge_base = {
    "academic_programs": {
        "questions": [
            "What academic programs do you offer?",
            "Tell me about the engineering department.",
            "What majors are available in the arts and sciences?",
            "Do you have a computer science program?",
            "What are the available graduate programs?",
        ],
        "answers": [
            "We offer a wide range of undergraduate and graduate programs in engineering, arts and sciences, business, and more. Check our website for a complete list.",
            "The engineering department offers programs in civil, mechanical, electrical, and computer engineering.",
            "The arts and sciences offer majors in history, English, biology, chemistry, and many more.",
            "Yes, we have a comprehensive computer science program with specializations in AI, software engineering, and data science.",
            "We offer graduate programs in business administration, engineering, computer science, and education.",
        ],
    },
    "admissions": {
        "questions": [
            "What are the admission requirements?",
            "What is the application deadline?",
            "How do I apply?",
            "What is the tuition fee?",
            "Do you offer scholarships?",
        ],
        "answers": [
            "Admission requirements vary depending on the program. Generally, we require high school transcripts, standardized test scores, and letters of recommendation.",
            "The application deadline for fall semester is typically March 1st. Please check our website for specific dates.",
            "You can apply online through our admissions portal on the university website.",
            "Tuition fees vary depending on the program and residency status. Please refer to the financial aid section of our website.",
            "Yes, we offer a variety of merit-based and need-based scholarships. Check our website for eligibility criteria and application procedures.",
        ],
    },
    "student_services": {
        "questions": [
            "What student services are available?",
            "Where is the library?",
            "How do I contact the student support center?",
            "What clubs and organizations are available?",
            "Where is the career services office?",
        ],
        "answers": [
            "We offer a range of student services, including academic advising, career counseling, library resources, and student support services.",
            "The library is located in the main building, near the student center.",
            "You can contact the student support center by phone at 555-1234 or by email at support@university.edu.",
            "We have numerous clubs and organizations, including academic clubs, sports clubs, and cultural clubs. Check our website for a complete list.",
            "The career services office is located in the student services building.",
        ],
    },
}

def preprocess_text(text):
    """Preprocesses the input text."""
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

def get_response(user_input):
    """Finds the best matching response from the knowledge base."""
    user_input_processed = preprocess_text(user_input)
    all_questions = []
    all_answers = []
    for category in knowledge_base.values():
        all_questions.extend(category["questions"])
        all_answers.extend(category["answers"])

    vectorizer = TfidfVectorizer()
    all_texts = [preprocess_text(question) for question in all_questions]
    all_texts.append(user_input_processed)
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    user_vector = tfidf_matrix[-1]
    question_vectors = tfidf_matrix[:-1]

    similarities = cosine_similarity(user_vector, question_vectors)
    best_match_index = similarities.argmax()

    if similarities[0, best_match_index] > 0.3:  # Threshold for similarity
        return all_answers[best_match_index]
    else:
        return "I'm sorry, I don't understand your question. Please rephrase or ask a different question."

def send_message():
    """Sends the user's message and displays the chatbot's response."""
    user_message = user_input.get()
    if user_message:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: " + user_message + "\n")
        response = get_response(user_message)
        chat_log.insert(tk.END, "Chatbot: " + response + "\n")
        chat_log.config(state=tk.DISABLED)
        user_input.delete(0, tk.END)
        chat_log.see(tk.END)

# GUI setup
root = tk.Tk()
root.title("University Chatbot")

chat_log = scrolledtext.ScrolledText(root, state=tk.DISABLED, height=20, width=50)
chat_log.pack(padx=10, pady=10)

user_input = tk.Entry(root, width=50)
user_input.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

root.mainloop()

# Evaluation:
# 1. Accuracy:
#    - The accuracy of responses depends on the quality and comprehensiveness of the knowledge base.
#    - The TF-IDF and cosine similarity approach works well for finding similar questions.
#    - The threshold value (0.3) for similarity can be adjusted to control the sensitivity of the chatbot.
#    - The chatbot handles simple questions effectively, but may struggle with complex or ambiguous queries.
# 2. Limitations:
#    - The chatbot relies on a static knowledge base and cannot answer questions outside its scope.
#    - It uses basic NLP techniques and may not understand complex sentence structures or context.
#    - It does not have the ability to learn or adapt over time.
# 3. Improvements:
#    - Expand the knowledge base to cover more topics and questions.
#    - Implement more advanced NLP techniques, such as named entity recognition and intent classification.
#    - Integrate a machine learning model for question answering, such as BERT or GPT.
#    - Add a feature to handle follow-up questions and maintain context.
#    - Implement a feedback mechanism to improve the chatbot's accuracy.
#    - Incorporate a database to store and retrieve information dynamically.
#    - Add a way to handle user specific information, such as student ID or course enrollment, by implementing user authentication.
#    - Use a more robust GUI, with better formatting of the chat log.
#    - Implement error handling for unexpected user input.