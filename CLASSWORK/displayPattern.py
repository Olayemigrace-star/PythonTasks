number = int(input("Enter a number\n"))

for number in range(number, 0, -1):
    for num in range(number, 0, -1):
        print(num, end= " ")
    print()
