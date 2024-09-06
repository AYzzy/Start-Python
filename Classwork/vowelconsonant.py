char =input("Enter a word: ")
count =0
counter=0
for i in char:
	if i =='a' or i=='e' or i=='i' or i =='o' or i =='u':
		count+=1
	else:
		counter+=1
print("Ther are ",count," vowels and ",counter," consonant in ", char )
			