principal = float(input("Enter the Principal: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time: "))

s_i = float((principal * time * rate) / 100)
amount = principal + s_i

print("The simple interest = ", s_i, "\nThe Amount = ", amount)

