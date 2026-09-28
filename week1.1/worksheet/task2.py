"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""
intflag = False
perYear = 0
savings = 0
interest = 0.0
plusInterest = 0.0
name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")
while not intflag:
    try:
        savings = int(input("How much would you like to save?"))
        perYear = 12*savings
        print(f"you will save £{perYear} per year.")
        intflag = True
        
    except:
        print(f"Please enter numbers only.")
    

interest = 0.008 * perYear
plusInterest = interest + perYear
print(f"Plus interest you will have £{plusInterest:.2f}.")


    


# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

