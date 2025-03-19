def classify_number():
    while True:
        try:
            # Prompt the user for input
            number = int(input("Enter an integer: "))

            # Classify the number
            if number > 0:
                return "Positive"
            elif number < 0:
                return "Negative"
            else:
                return "Zero"
        except ValueError:
            # Handle invalid input (non-integer)
            print("Invalid input. Please enter a valid integer.")

result = classify_number()
print(f"The number is: {result}")