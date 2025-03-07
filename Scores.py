score = float(input("Enter the student's score: "))
if 75 <= score <= 100:
    print("A")
elif 60 <= score < 75:
    print("B")
elif 50 <= score < 60:
    print("C")
elif 40 <= score < 50:
    print("D")
elif 30 <= score < 40:
    print("E")
elif 0 <= score < 40:
    print ("F")
else :
    print("Invalid score")
print("End of program")