count = 0
sum_of_numbers = 0
number_input = int(input("Enter your number: "))

for number_input in range(1, 5):
	number_input = int(input("Enter your number: "))
	sum_of_numbers += number_input
	count += 1
	average_of_numbers = sum_of_numbers/count
	product_of_numbers = number_input * number_input * number_input
	
	
print("The sum of all numbers is", sum_of_numbers)
print("The average of all numbers is", average_of_numbers)
print("The product of all numbers is", product_of_numbers)
