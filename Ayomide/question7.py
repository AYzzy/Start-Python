#prompt user to input the amount in the account currently
#  prompt user to input the years which the money as used in the account 
# prompt user to input the monthly amount compounding on it 


final_account = int(input("Enter the amount of money in the account: "))
years = int(input("Enter the number of years the money as been in the account : "))
interest_rate = int(input("Enter the monthly interest rate compounding on it : "))

month = years * 12
monthly_interest_rate = interest_rate /100

initial_deposit_amount = final_account/(1 + monthly_interest_rate) ** month

print(f'The final_account is {final_account} and as been fixed for {years}years, at a monthly interest of {interest_rate}%.The initial deposit is {initial_deposit_amount:.3f}')