largest = 0
second_largest = 0

for count in range(4):
	num = int(input("Enter a number: "))
	if num> largest:
		second_largest = largest
		largest = num
	elif num < largest and num > second_largest:
		second_largest = num

print("The largest number is: ", largest)
print("The second_largest number is: ", second_largest)