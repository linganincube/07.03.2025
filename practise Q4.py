# list of the names to write to the file
names = ["Lingani","Future","Skhue"  ]

# Write the names to the file using the 'with' statement
with open ("names.txt","w") as file:
     for name in names:
         file.write(name + "\n") # write each name followed by a newline

# Read names from this file and print them to console
with open("names.txt","r") as file:
    print("Name in file:")
    for line in file:
        print(line.strip()) # use strip to remove any trailing newline characters
