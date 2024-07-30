def reverse(numbers):
	max =0
	for count in numbers:
		for counter in numbers:
			if(count > counter):
				max = count
				count = counter
				counter = max

	return numbers


print(reverse([1,2,3,4,5,6]))