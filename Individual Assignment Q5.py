# Sample list of Celsius temperatures
celsius_temps = [0, 15, 20, 35, 40]

# Convert to Fahrenheit using map and lambda
fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))

# Print the results
print("Celsius Temperatures:", celsius_temps)
print("Fahrenheit Temperatures:", fahrenheit_temps)