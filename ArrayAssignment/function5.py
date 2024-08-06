def even_position(even_list):
	length = len(even_list)
	new_even = []
	for number in range(length):
		if number % 2 == 0:
			new_even.append(even_list[number])
			
	return new_even


print(even_position([45, 67, 43, 31, 78]))
			