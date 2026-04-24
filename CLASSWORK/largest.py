def largest(number_one, number_two, number_three):

    if number_one > number_two and number_one > number_three:
        largest_number = number_one

    elif number_two > number_three and number_two > number_one:
        largest_number = number_two

    elif number_three > number_one and number_three > number_two:
        largest_number = number_three

    return largest_number - 1

print(largest(3, 2, 1))=-                
