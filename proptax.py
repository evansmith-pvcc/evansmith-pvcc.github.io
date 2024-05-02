# Name: Evan Smith
# Prog Purpose: This program finds the cost of taxes
import datetime

############## Define global variables ##############
TAX_RATE = 0.044
DUE_DATE = 'JUNE 05'
RELIEF_RATE = 0.3

# Define global variables
assesed_value = 0.0
relief_amount = 0.0
relief_tf = 2
annual_amount = 0.0
total_due = 0.0

############## Define program functions ##############
def main():
    more = True
    while more:
        print('**** PERSONAL PROPERTY TAX BILL ****')
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to calculate tax for another vehicle (Y or N)? ")
        if yesno.upper() == "N":
            more = False
            print("Personal property tax is due " + DUE_DATE)

def get_user_data():
    global assesed_value, relief_tf
    assesed_value = float(input("\nAssessed value of the vehicle: $"))
    relief_tf = int(input("\nIs your vehicle eligible for tax relief? (1 for YES, 2 for NO): "))

def perform_calculations():
    global relief_amount, annual_amount, total_due
    if relief_tf == 1:
        relief_amount = assesed_value * RELIEF_RATE * TAX_RATE
    else:
        relief_amount = 0
    annual_amount = (assesed_value * TAX_RATE) - relief_amount
    total_due = annual_amount / 2

def display_results():
    currency = '{:,.2f}'
    line = '-----------------------------'
    full_date = str(datetime.datetime.now())
    short_date = full_date[0:16]
    print(line)
    print('**** PERSONAL PROPERTY TAX BILL ****')
    print('Date/Time: ' + short_date)
    print(line)
    print('Assessed Value        $' + currency.format(assesed_value))
    print('Relief Amount        $' + currency.format(relief_amount))
    print('Full Annual Amount   $' + currency.format(annual_amount))
    print(line)
    print('Total Due            $' + currency.format(total_due))


main()
