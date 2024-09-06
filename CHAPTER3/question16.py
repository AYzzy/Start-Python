largest = float('-inf')
second_large = float('-inf')

for count in range(10):

	num =float(input("Enter number: "))

	if num >largest:
		second_large = largest
		largest = num
	elif num >second_large:
		second_largest = num
print("The Largest number is: ",largest )
print("The second_large is: ", second_large)