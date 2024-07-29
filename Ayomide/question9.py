#prompt user to enter name
#prompt user to enter numbers hours worked in a week
#prompt user to enter the hourly pay rate
#Enter Federal tax withholding rate
#Enter state tax withholding rate
#print the total deduction 
#print net pay


name = input("Enter employee's names:")
time_rate = int(input('Enter numbers hours worked in a week: '))
pay_per_hour = float(input('Enter the hourly pay rate: '))
federal_tax = int(input('Enter Federal tax withholding rate: '))
state_tax = int(input('state tax withholding rate:'))

total_federal_tax = federal_tax/100
total_state_tax = state_tax/100

actual_pay = time_rate * pay_per_hour

result_federal_tax = actual_pay * total_federal_tax
result_state_tax = actual_pay * total_state_tax

total_tax = result_federal_tax + result_state_tax

net_pay = actual_pay - total_tax

print("")
print(name)
print('Hours worked: ',time_rate)
print('fedral rate',total_federal_tax)
print('state rate ',total_state_tax)
print('Pay Rate: ',pay_per_hour)
print('Gross pay: ',                                                                                                                                                                                                                   actual_pay)
print ("")
print('Deduction')
print(f'Federal Withholding {federal_tax}%:${result_federal_tax} ')
print(f'State Withholding {state_tax}%: ${result_state_tax}')
print('Total Deduction: $', total_tax)
print('Net pay: $',net_pay)