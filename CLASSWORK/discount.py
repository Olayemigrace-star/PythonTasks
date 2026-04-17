'''if user purchases between 1000 and 10000
Do a 5% discount
else if user purchases between 10000 to 50000
Do a 10% discount
if user purchases above 50000
Do a 20% discount

'''
total_amount = int(input("Enter the amount of purchased items "));
int firstdiscount = (amount - (amount * 0.05));
int seconddiscount = (amount - (amount * 0.1));
int thirddiscount = (amount - (amount * 0.2));


if total_amount >= 1000 and total_amount <=10000:{
print("Your prize is ", firstdiscount);
} 

if total_amount >= 10000 and total_amount <= 50000:{
print("Your prize is ", seconddiscount);
}
if total_amount > 50000:{
print("Your prize is ", thirddiscount);
}


