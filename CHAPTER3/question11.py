total_miles = 0.0
total_gallons = 0.0
print("Hola, Welcome to Gas Millage Calculator")
print("Enter the miles driven and gallons used for each tankful (enter '' to fyesinish):")

while True:
	user_input = input("Enter miles driven (or 'yes' to finish): ")
	if user_input.lower() == 'yes':
		break
	miles_driven = float(user_input)

	gallons_used = float(input("Enter gallons used: "))

	if gallons_used > 0:
		mpg = miles_driven / gallons_used
		print(f"Miles per gallon for this tank: {mpg:.2f}")
   
		total_miles += miles_driven
		total_gallons += gallons_used
	else:
		print("Invaid input")


if total_gallons > 0:
	overall_mpg = total_miles / total_gallons
	print(f"\nThe Overall average miles/gallon was: {overall_mpg:.2f}")
else:
	print("\nBye Bye.")