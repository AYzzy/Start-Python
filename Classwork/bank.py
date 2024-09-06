balance =0
number=0
amount =0
while (number!= -1):
	number=int(input("Enter 1 to deposit and 2 to withdraw and 3 to check balance: "))
	if number==1:
		deposit = int(input("Enter amount to deposit: "))
		balance+=deposit
		if(deposit<0):
			print("Amount not accepted")
	#number=int(input("Enter 1 to deposit and 2 to withdraw and 3 for balance: "))			
	
	if number ==2:
		withdraw =(int(input("Enter amount to withdraw: ")))
		if(withdraw >=balance  ):
			amount=balance
			balance-=withdraw
			print("EXceeded balance")
		
	if number ==3:	
		print(amount)
		
print("Total bal is " , amount)		