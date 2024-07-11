number = int(input("Enter score: "))
if(number<0):
	print("Invalid input")
elif (number >=75):
	print("A")
elif(number >=65):
	print("B")
elif(number >=50):
	print("C")
elif(number >=40):
	print("D")
else:
	print("F")