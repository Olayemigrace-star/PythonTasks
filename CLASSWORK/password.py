'''Ask the user for their password
if password length is less than 8 
print very weak
if password is 8
print weak
if password is between 8 and 16
print strong
if password is greater than 16
print very strong
'''

password = input("Enter your preferred Password ")
if len(password) < 8:
    print(" The Password entered is very weak ")
if len(password) == 8:
    print("The Password entered is Weak ")
if len(password) > 8 and len(password) >= 16:
    print("Password entered is Strong")
if len(password) > 16:
    print("Password entered is very Strong ")


