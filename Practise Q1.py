def classify_number(num):
    """
    Classifies the given integer as 'Positive', 'Negative', or 'Zero'.

    Parameters:
        num (int): The integer to classify.

    Returns:
        str: 'Positive', 'Negative', or 'Zero'.
    """
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


def main():
    """
    Repeatedly prompts the user for an integer input and classifies it.
    """
    while True:
        user_input = input("Enter an integer: ")
        try:
            # Attempt to convert the input to an integer
            number = int(user_input)
            # Call the classify_number function and display the result
            result = classify_number(number)
            print(f"The number is {result}.")
            break  # Exit the loop after successful classification
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter a valid integer.")


# Run the program
if __name__ == "__main__":
    main()


