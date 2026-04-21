print("number  square  cube")

for number in range(0, 6):
    print(number, end="      ")
    squares = number * number
    print(squares, end="        ")
    cubes = number * number * number
    print(cubes)    
