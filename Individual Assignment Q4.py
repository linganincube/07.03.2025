# Define a list of names to write to the file
names = ["Lingani", "Winnie", "Sikhulekile", "Kudzai", "Musilahane"]

# Write the names to a file
with open('names.txt', 'w') as file:
    for name in names:
        file.write(f"{name}\n")  # Write each name on a new line

# Read the names from the file and print them
with open('names.txt', 'r') as file:
    print("Names in the file:")
    for line in file:
        print(line.strip())  # Remove any leading/trailing whitespace or newlines