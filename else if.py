hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
if hours <= 35:
    pay = hours * rate
else:
    pay = 35 * rate
    overtime = hours - 35
    overtime_pay = overtime * (rate * 1.5)
    gross_pay = pay + overtime_pay
    print("Gross Pay", gross_pay)