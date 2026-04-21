print("   Multiplication Table ")

for number in range(1, 10):
    print(number, end=" | ")
    for num in range(1, 10):
        product = number * num
        print(f"{product:>2}", end= " ")
    print()
