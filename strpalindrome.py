name = "cars"
count = 0
for characters in name:
    count +=1
    
    
print(count)
print(len(name))



text = input("Enter a string: ")

if text == text[::-1]:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")


text = "world"
reversed_text = ""

# Loop through each character and add it to the front
for char in text:
    reversed_text = char + reversed_text

print(reversed_text)  # "dlrow"

