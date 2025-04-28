def get_valid_number():
    """
    Repeatedly prompts the user for input until a valid number is entered.

    Returns:
        float:The valid number entered by the user.
    """

    while True:
        user_input = input("Faka inumber eright: ")
        try:
            # Attempt to convert input to float
            number = float(user_input)
            print(f"Good boy, the number entered is {number}")
            return number
        except ValueError:
            #Handle invalid input
            print("Fuseki uyahlanya.Please enter a number.")

# Run the program
if __name__ == "__main__":
    get_valid_number()

