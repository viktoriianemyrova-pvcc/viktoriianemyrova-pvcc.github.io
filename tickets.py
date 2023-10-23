# Name: Viktoriia Nemyrova
# Prog Purpose: This program finds the cost of movie tickets
#   Price for one ticket: $10.99
#   Price for one popcorn: $8.99
#   Price for one drink: $4.99
#   Sales tax rate: 5.5%

import datetime

############## define global variables ##############
# define tax rate and price
SALES_TAX_RATE = .055
PR_TICKETS = 10.99
PR_POPCORN = 8.99
PR_DRINKS = 4.99

# define global variables
num_tickets = 0
num_popcorn = 0
num_drinks = 0
cost_tickets = 0
cost_popcorn = 0
cost_drinks = 0
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

        yesno = input("\nWould you like to order again (Y or N)?" )
        if yesno == "N" or yesno == "n":
            more_tickets = False
            print("Thank you for order. Enjoy your movie!")
    
def get_user_data():
    global num_tickets, num_popcorn, num_drinks
    num_tickets = int(input("Number of movie tickets: "))
    num_popcorn = int(input("Number of popcorn buckets: "))
    num_drinks = int(input("Number of drinks bottles: "))

def perform_calculations():
    global subtotal, sales_tax, total, cost_tickets, cost_popcorn, cost_drinks
    cost_tickets = num_tickets * PR_TICKETS
    cost_popcorn = num_popcorn * PR_POPCORN
    cost_drinks = num_drinks * PR_DRINKS
    subtotal = cost_tickets + cost_popcorn + cost_drinks
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    myfloat = '8,.2f'
    print('-----------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighbothood movie house')
    print('-----------------------------')
    print('Tickets      $ ' + format(cost_tickets, myfloat))
    print('Popcorn      $ ' + format(cost_popcorn, myfloat))
    print('Drinks       $ ' + format(cost_drinks, myfloat))
    print('Sales Tax    $ ' + format(sales_tax, myfloat))
    print('Total        $ ' + format(total, myfloat))
    print('-----------------------------')
    print(str(datetime.datetime.now()))

############## call on main program to execute ##############
main()
















          
