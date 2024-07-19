import random

print("Hello! Welcome to the Guess The Number Game")

number = random.randint(1, 1000)
total = 0

while True:
	num = int(input("Enter a number between 1 and 1000 and -1 to end: "))
    
	if num == -1:
		print("Game ended. The number was:", number)
		break
    
	if num < 1 or num > 1000:
		print("Use your head, enter a number between 1 and 1000")
	elif num > number:
		print("Too high. Try again")
	elif num < number:
		print("Too low. Try again")
	else:
		print("Congratulations! You guessed the number!")
		break

	total +=1
	print("You have tried the game ",total,"times")

	if total>=10:
		print("You have tried , To try again press 1 and 2 to end")
		
	
