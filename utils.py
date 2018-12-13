from random import randint

def generateCode():
	return randint(1000, 9999)

def numberFormatter(number):
	if number.startswith('0'):
		number = "+254" + number[1:]
	elif number.startswith('254'):
		number = "+" + number
	elif number.startswith('+'):
		number = number
	else:
		return None

	return number