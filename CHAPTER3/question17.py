for count in range(0,6):
	for counter in range(count):
		print("*", end =' ')
	print()
print()

for num in range(6,0, -1):
	for num1 in range(num):
		print("*", end =' ')
	print()
print()


for i in range(0, 6):
	for j in range(7 - i):
		print(' ', end='')
	for j in range(i):
		print('*', end='')
	print()
print()

for i in range(6, 0, -1):
	for j in range(7 - i):
		print(' ', end='')
	for j in range(i):
		print('*', end='')
	print()