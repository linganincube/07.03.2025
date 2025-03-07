months = float(input("number of months"))
rate = float(input("monthly rate"))
if months <= 12:
    pay = months * rate
else:
    pay = months * rate
    long_time = months - 12
    long_time_pay = long_time * (rate * 1.5)
    gross_pay = pay + long_time_pay
print(f"Gross pay: ${gross_pay:.2f}")
