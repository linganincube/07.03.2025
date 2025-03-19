def calculate_average(*args):
    """
    Calculate the average of a variable number of numeric arguments.

    Parameters:
        *args (float or int): A variable number of numeric arguments.

    Returns:
        float: The average of the provided numbers.

    Example:
        >>> calculate_average(10, 20, 30)
        20.0
        >>> calculate_average(5, 15, 25, 35)
        20.0
    """
    if not args:  # Handle the case where no arguments are provided
        return 0.0

    total = sum(args)  # Calculate the sum of all arguments
    count = len(args)  # Count the number of arguments
    average = total / count  # Calculate the average
    return average


# Example usage
result = calculate_average(10, 20, 30, 40)
print(f"The average is: {result}")