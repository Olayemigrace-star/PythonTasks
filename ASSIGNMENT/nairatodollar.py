def naira_to_dollar(dollar_amount):
	if type (dollar_amount) != float and type (dollar_amount) != int:
		return"invalid input"
	result = dollar_amount * 1550
	return result
	
print (naira_to_dollar(600))
