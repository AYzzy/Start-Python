for num in range(1000,3000):
	digit = num//1000
	digit1 = (num/100)%10
	digit2 = (num//10)%10
	digit3 = num%10
	
	if digit % 2==0 and digit1 % 2==0 and digit2 % 2==0 and digit3 % 2==0:
		
		print(num)