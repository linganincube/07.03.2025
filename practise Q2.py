def calculate_average(*args):
    """
    Calculate the average of a variable number of numerical arguments

    Parameters:
        *args: Variable number of numerical arguments(integers or floats)

    Returns:
    float: Average value of variable number of numerical arguments.Return 0 if no numerical arguments were entered.
    """
    # Check if any arguments are provided
    if not args:
        return 0 # return 0 if no arguments are given

    # Calculate the sum of all arguments
    total = sum(args)

    # Calculate the count of arguments
    count = len(args)

    # Return the average
    return total/count


print(calculate_average(10, 20, 30))  # Output: 20.0