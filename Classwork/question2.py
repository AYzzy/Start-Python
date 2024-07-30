words = input("Enter a word:")
count=0
counter=0

for num in words:
	
	if(num.isdigit()):
		count+=1
	else:
		counter = counter + 1

print("letters are",counter,"numbers are ",count)