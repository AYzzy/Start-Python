import random

print("Hello! Welcome to the Guess The Number Game")

number = random.randint(1, 1000)
total = 0
guess=0

while guess != number:
	guess = int(input("Enter a number:"))
	if guess <1 or guess >1000:
		print("Use your head, enter a number between 1 and 1000")
	elif guess > number:
		print("Too high. Try again")
	elif guess < number:
		print("Too low. Try again")
	else:
		print("Congratulations! You guessed the number!")
		continue
	total+=1
	if(total == 10):
		print("You have tried the game ",total,"times")

	