approx =1
factorial =1

for i in range(1, 10):
	factorial *=i
	approx +=1 /factorial

print(f"The approximation of 10 terms: {approx}")