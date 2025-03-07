year_input = input("Enter a year: ")
try:
    year = int(year_input)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
    print("Invalid input. Please enter a valid year.")
