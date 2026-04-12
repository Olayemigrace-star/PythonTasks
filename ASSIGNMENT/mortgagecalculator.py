principal = float(input("Enter the Principal amount: "))
r = float(input("Enter the interest rate: "))
d = float(input("Enter the duration of the loan: "))
rate = r / 1200
duration = d * 12
monthlymortgage = float((principal * (rate * ((1 + rate) ** duration)) ) / ( ((1 + rate) ** duration)) - 1)

print("Your monthly payment is = ", monthlymortgage)

