# Define custom exception
class NegativeNumberError(Exception):
    """Exception raised for negative input values."""
    pass


# Define validation function
def check_positive(number):
    """
    Check if a number is positive.

    Args:
        number (int/float): Number to validate

    Returns:
        int/float: Original number if positive

    Raises:
        NegativeNumberError: If input number is negative
    """
    if number < 0:
        raise NegativeNumberError(f"Negative number not allowed: {number}")
    return number


# Demonstration with try/except blocks
if __name__ == "__main__":
    # Test valid input
    try:
        result = check_positive(15)
        print(f"Valid number: {result}")
    except NegativeNumberError as e:
        print(e)

