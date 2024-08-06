def reverse_list (number_list):
	length = len(number_list)
	new_reverse =[]
	for number in range(length-1, -1, -1):
		new_reverse.append(number_list[number])
		
	return new_reverse



result = reverse_list([1, 2, 3, 4, 5])
print(result)
	