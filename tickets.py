# Name: Viktoriia Nemyrova
# Prog Purpose: This program finds the cost of movie tickets
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime

############## define global variables ##############
# define tax rate and price
SALES_TAX_RATE = .055
PR_TICKETS = 10.00

# define global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

############## define program functions ##############
def main():
    
    more_tickets = True

    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to order again (Y or N)?:" )
        if askAgain.upper() == "N" or askAgain == "n":
            more_tickets = False
            print("Thank you for order. Enjoy your movie!")
    
def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKETS
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('-----------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighbothood movie house')
    print('-----------------------------')
    print('Tickets      $ ' + format(subtotal,'8,.2f'))
    print('Sales Tax    $ ' + format(sales_tax,'8,.2f'))
    print('Total        $ ' + format(total,'8,.2f'))
    print('-----------------------------')
    print(str(datetime.datetime.now()))

############## call on main program to execute ##############
main()
















          
