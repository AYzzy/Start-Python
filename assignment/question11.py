number =int(input("Enter 5 input: "))

number1= number//10000
number2=(number//1000)%10
number3 = (number//100)%10
number4 =(number//10)%10
number5=number%10

print(number1,"   ", number2,"   ", number3,"   ", number4,"   ", number5,"   ")