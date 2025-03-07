char = input("Enter a letter: ").strip()
if len(char) != 1 or not char.isalpha():
    print("Invalid input. Please enter a single alphabetic character.")
elif char.upper() == "Z":
    print("Excluded letter: Z")
elif char.isupper():
    print("Uppercase letter:", char)
else:
    print("Lowercase letter:", char)
