number = int(input("Enter a five-digit integer: "))


if number < 10000 or number > 99999:
	print("Please enter a valid five-digit integer.")
else:
	 print("Digits separated:")

temp = number
for i in range(5):
	digit = temp // (10 ** (4 - i))  
	print(digit)
	temp = temp % (10 ** (4 - i))