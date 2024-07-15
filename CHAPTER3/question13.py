num = int(input("Enter an integer: "))

factorial = 1

if num < 0:
	print("invalid input.")
elif num == 0:
	print("Factorial of 0 is 1.")
else:
	for i in range(1, num + 1):
		factorial *= i
	print(f"The factorial of {num} is: {factorial}")