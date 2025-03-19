while True:
    try:
        # Get user input and attempt conversion to float
        number = float(input("Please enter a number: "))
        break  # Exit loop if conversion succeeds
    except ValueError:
        # Handle invalid input
        print("Invalid input! Please enter a valid number.")

# Once valid input is received
print(f"Success! You entered: {number}")