def total_addition(number_list):
	length = len(number_list)   
	addition = 0
	for add in range(0, length - 1):
		addition += number_list[add]
		
	return addition




result = total_addition(number_list = [5, 6, 7, 68, 45, 34, 2,  67, 21])
print(result)