def discount_in_price(price, discount):
	return price - (price * (discount/100))


price = int(input("Enter price:")

discount = int(input("Enter the discount percentage:"))

actual_amount = discount_in_price(price, discount)

print(actual_amount)