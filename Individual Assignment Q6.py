def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")

# Example usage:
print(divide_numbers(20, "45"))  # Should print 5.0


