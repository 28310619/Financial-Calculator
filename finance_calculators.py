import math

''' This program allows the user to calculate their interest on an investment.
 The programme uses if,elif and else to determine the outcome.
 The programme output is investment amount or amount of repayment per month
 according to certain individual conditions.'''

# Pick a choice of investment.
print("Investment - To calculate the amount of interest you'll earn on your investment")
print("Bond       - To calculate the amount you'll have to pay on a home loan \n \n")

choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# The investment block of code produces simple interest and compounded interest in your investment. 
if choice == 'investment': 
    amount = float(input("\nHow much money would you like to deposit today? \n> £"))
    interest_rate = float(input("\nHow much is the interest rate as a percentage? \nPlease enter the number only: "))
    length_of_investment = float(input("\nHow many years do you plan on investing for? \n>"))

    simple_interest = amount * (1 + (interest_rate / 100) * length_of_investment)
    compounded_interest = amount * math.pow((1 + interest_rate / 100), length_of_investment)
    
    simple_interest = float("{:.2f}".format(simple_interest))
    compounded_interest = float("{:.2f}".format(compounded_interest))

# Asks user for choice of interest calculation after both simple and compounded interest are calculated
    simple_or_compounded = input("\nPlease choose 'simple' or 'compounded' interest: ").lower()

    if simple_or_compounded == 'simple':
        print(f'\nYour simple interest investment is: £{simple_interest}')
    
    elif simple_or_compounded == 'compounded':
        print(f'\nYour compounded interest investment is: £{compounded_interest}')

# The elif statement evaluates and produces a result of how much money we need to repay monthly.   
elif choice == 'bond':
    house_value = float(input("\nHow much is the current house value? \n £"))
    interest_rate = (float(input("\nHow much is the interest rate? \n")) / 100)
    num_months = float(input("\nNumber of months you plan to repay the bond? \n"))
    repayment = (((interest_rate / 12) / 100) * house_value) / (1 - (1 + ((interest_rate / 12) / 100)) ** (- num_months))
    repayment = float("{:.2f}".format(repayment))
    print(f'\nYour repayment is: £{repayment} per month.')

# The else statement executes when anything other than our choices are inputted.
else:
    print("Please select either 'investment' or 'bond' only.")
