print("Goodday, Welcome to the mortgage calculator ")

name = imput("PLease input your name: ")

principal = int(input("Enter the amount you wish to borrow:  "))
rate =int(input("Enter the annual insterest rate:  "))
duration =int(input("Enter the duration of the loan: "))


total = principal * (rate (1 + rate)**duration/ (1+ rate)**duration -1

print("Dear ",name, " ,Your monthly payment is $ ", total) 