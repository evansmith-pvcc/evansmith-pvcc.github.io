# Name: Evan Smith
# Prog Purpose: This program finds the cost of a meal at Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime

############ define global variables ############
# define tax rate, service fee, and prices
ADULT_MEAL = 19.95
CHILD_MEAL = 11.95
SERVICE_FEE = 0.1
SALES_TAX_RATE = 0.062


# define global variables
num_adult_meals = 0
num_child_meals = 0
subtotal = 0
sales_tax = 0
service_fee = 0
total = 0

############### define program functions ###############
def main():

    more_meals = True
    
    while more_meals:
        get_user_data()
        perform_calculations ()
        display_results ()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno == "N" or yesno == "n":
            more_meals = False
            print("Thank you for your order. Enjoy your meal!")

def get_user_data():
    global num_adult_meals, num_child_meals
    num_adult_meals = int(input("Number of adult meals: "))
    num_child_meals = int(input("Number of child meals: "))
    
def perform_calculations ():
    global subtotal, sales_tax, service_fee, total
    subtotal = (num_adult_meals * ADULT_MEAL)+(num_child_meals * CHILD_MEAL)
    sales_tax = subtotal * SALES_TAX_RATE
    service_fee = subtotal * SERVICE_FEE
    total = subtotal + sales_tax + service_fee

def display_results():
    print('--------------------------')
    print('**BRANCH BARBEQUE BUFFET**')
    print('*Your neighborhood buffet*')
    print('--------------------------')
    print('Meals       $ ' + format(subtotal,'8,.2f'))
    print('Sales Tax   $ ' + format(sales_tax,'8,.2f'))
    print('Sales Tax   $ ' + format(sales_tax,'8,.2f'))
    print('Total       $ ' + format(total,'8,.2f'))
    print('--------------------------')
    print(str(datetime.datetime.now()))
######## call on main program to execute ########
main()
