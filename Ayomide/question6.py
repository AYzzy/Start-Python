#prompt user to enter minutes 
#divide the minutes by 525600 to get the year 

minutes = int(input('Enter the minutes:'))

years = minutes // 525600
days = minutes / 525600 % 43800

print(f'{years} years {days} days')