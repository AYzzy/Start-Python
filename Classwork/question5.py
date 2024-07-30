def reverse(number):
	digit1 = number//100
	digit2 = (number//10)%10
	digit3 = number%10
	numbers =str(digit3) + str(digit2) + str(digit1)
	return numbers

print(reverse(879))