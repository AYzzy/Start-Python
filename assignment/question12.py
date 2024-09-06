principal = 1000
rate = 0.07
year1 = 10
year2 = 20
year3 = 30

area1 = principal * (1 + rate) ** year1
area2 = principal * (1 + rate) ** year2
area3 = principal * (1 + rate) ** year3


print("The principal is $1000, the rate of return is 7%, and we are calculating the investment return for 10, 20, and 30 years:")
print("Interest return for 10 years: $", area1)
print("Interest return for 20 years: $", area2)
print("Interest return for 30 years: $", area3)
