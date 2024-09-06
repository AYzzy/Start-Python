num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))

sum = num1+num2+ num3
average = sum/3
product = num1 * num2 * num3

print(sum)
print(average)
print(product)

if num1 > num2 and num1 >num3:
	print(num1," is the greatest")
elif num2 > num1 and num2 >num3:
	print(num2," is the greatest")
else:
	print(num3," is the greatest")

if num1 < num2 and num1 <num3:
	print(num1," is the smallest")
elif num2 < num1 and num2 < num3:
	print(num2," is the smallest")
else:
	print(num3," is the smallest")