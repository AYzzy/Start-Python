print("Goodday, Welcome to the mortgage calculator ")

name = input("PLease input your name: ")

principal = int(input("Enter the amount you wish to borrow:$ "))
rate =int(input("Enter the annual insterest rate:  "))
duration =int(input("Enter the duration of the loan: "))

rate2=rate/1000
total = principal *rate2*( (1 + rate2)**duration)/ (1+ rate2)**duration -1

print(f"Dear {name},Your monthly payment is ${ total:.2f}") 