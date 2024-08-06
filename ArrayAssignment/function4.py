def odd_position(userinput_list):
	length = len(userinput_list)
	odd_number = []
	for number in range(0, length, 1):
		if number % 2 == 1:
			odd_number.append(userinput_list[number])
	return odd_number



print(odd_position([12, 3, 5, 67, 45, 36]))


			
	