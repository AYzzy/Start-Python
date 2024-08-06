def largest_number(number):
	largest =0
	for index in number:
		if index > largest:
			largest = index
	return largest



print(largest_number([4,6,9,5,15,1]))