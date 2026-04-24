for numbers in range(0, 51):
    if(numbers % 3 == 0):
        print("Fizz");
    elif(numbers % 5 == 0):
        print("Buzz ");
    elif(numbers % 3 and numbers % 5== 0):
        print(numbers + ". FizzBuzz");
