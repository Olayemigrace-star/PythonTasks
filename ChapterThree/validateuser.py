passes = 0

for count in range(1, 11):   
    result = int(input("Enter 1 for pass and 2 for fail: "))  
    while(result != 1 and result != 2):     
        result = int(input("Enter 1 for pass and 2 for fail: "))

    if result == 1:
       passes += 1
print("passes =", passes)
print("count =", count)
failures = count - passes
print("failure =", failure)
       

