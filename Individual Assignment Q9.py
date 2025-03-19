import re

# I. Extract email addresses
def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

# II. Validate date format
def validate_date(date_str):
    date_pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
    return bool(re.match(date_pattern, date_str))

# III. Replace words
def replace_words(text, old_word, new_word):
    return re.sub(r'\b' + re.escape(old_word) + r'\b', new_word, text)

# IV. Split by non-alphanumeric
def split_by_non_alphanumeric(text):
    return re.split(r'\W+', text)

# Demonstration
if __name__ == "__main__":
    # Test data
    sample_text = "Contact us at linganincube@gmail.com or lncube@afcholdings.co.zw. For urgent matters, email emergency@cuz.ac.zw."
    date_to_check = "2023-05-115"
    text_to_replace = "The quick brown fox jumps over the lazy dog. Jumps!"
    text_to_split = "Hello, world! This is a test: 1983."

    # I. Extract emails
    print("Extracted emails:", extract_emails(sample_text))

    # II. Validate date
    print(f"Is '{date_to_check}' valid?", validate_date(date_to_check))

    # III. Replace words
    print("Replaced text:", replace_words(text_to_replace, "jumps", "crawl"))

    # IV. Split by non-alphanumeric
    print("Split text:", split_by_non_alphanumeric(text_to_split))