import random

def generate_random_list(length=10, min_val=1, max_val=100):
    """Generates a list of random integers."""
    random_list = [random.randint(min_val, max_val) for _ in range(length)]
    return random_list

def calculate_average(number_list):
    """Calculates the average of a list of numbers."""
    if not number_list:
        return 0  # Return 0 for an empty list to avoid ZeroDivisionError
    return sum(number_list) / len(number_list)

def main():
    """Main function to generate the list and calculate the average."""
    random_numbers = generate_random_list()
    print("Generated random numbers:", random_numbers)

    average = calculate_average(random_numbers)
    print("Average:", average)

if __name__ == "__main__":
    main()