number = int(input("Enter first integer: "))
number2 = int(input("Enter second integer: "))

if number == number2:
	print(number,'is equal to ', number2)
elif number <= number2:
	print(number, ' is less than or equal to ', number2)
else:
	print(number, 'is greater than or equal to ', number2)