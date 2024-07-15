principal = 1000.0

rate = 0.07

print("Year \t Total_value")

for year in range(1, 31):
	total_value = principal * (1 + rate) ** year
	print(f"{year} \t ${total_value:.2f}")