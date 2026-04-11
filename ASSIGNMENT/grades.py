grades = int(input("Enter your grade from 0 - 100: "))

if grades >= 90 and grades <= 100:
    print("A")

elif grades <= 89 and grades >= 80:
    print("B")

elif grades <= 79 and grades >= 70:
    print("C")

elif grades <= 69 and grades >= 60:
    print("D")

else:
    print("F")
