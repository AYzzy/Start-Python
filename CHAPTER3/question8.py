sum=0
average=0
product=1
num=3
smallest=0
for i in range(num):
	number= int(input("Enter an integer: "))
	sum+=number
	average=sum/num
	product *=number
	

print ("The total sum is: ",sum )
print("The averge is: ",average)
print("The product is: ",product)	
print("The smallest number :", number)