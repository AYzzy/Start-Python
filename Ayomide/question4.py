#prompt user to input the subtotal
# prompt user to input the gratuity rate in percentage
#multipy the subtotal against the gratuity rate
#sum the result to the subtotal

subtotal = int(input("Enter the subtotal:"))
gratuity_rate = int(input("Enter the gratuity_rate :"))

total_gratuity_rate = gratuity_rate/100

result = subtotal * total_gratuity_rate

total = subtotal + result

print(f'The subtotal is {subtotal} and the gratuity_rate is {gratuity_rate}% the total subtotal is {total}')

