# Name: Viktoriia Nemyrova, Carter Kardell, 
# Prog Purpose: This program finds the cost of movie tickets
#   Price for one ticket: $10.99
#   Price for one popcorn: $8.99
#   Price for one drink: $4.99
#   Sales tax rate: 5.5%

import datetime

############## define global variables ##############
# define tax rate and price
SALES_TAX_RATE = .062
SERVICE_FEE = .1
PR_ADULTS = 19.95
PR_CHILDREN = 11.95


# define global variables
num_adults = 0
num_children = 0
num_drinks = 0
cost_adults = 0
cost_children = 0
subtotal = 0
sales_tax = 0
service_fee = 0
total = 0

############## define program functions ##############
def main():
    
    more = True


    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nIs there another order (Y or N)? " )
        if yesno == "N" or yesno == "n":
            more = False
            print("Thank you for order. Enjoy your food!")
            

def get_user_data():
    global num_adults, num_children  
    num_adults = int(input("Number of adults: "))
    num_children = int(input("Number of children: "))
    

def perform_calculations():
    global subtotal, sales_tax, service_fee, total, cost_adults, cost_children
    cost_adults = num_adults* PR_ADULTS
    cost_children = num_children * PR_CHILDREN
    subtotal = cost_adults + cost_children
    sales_tax = subtotal * SALES_TAX_RATE
    service_fee= subtotal * SERVICE_FEE
    total = subtotal + sales_tax + service_fee

def display_results():
    myfloat = '8,.2f'
    line= "--------------------------------"
    print(line)
    print('**** Branch Barbecue Buffet ****')
    print(line)
    print('Adults       $ ' + format(cost_adults, myfloat))
    print('Children     $ ' + format(cost_children, myfloat))
    print('Sales Tax    $ ' + format(sales_tax, myfloat))
    print('Service Fee  $ ' + format(service_fee, myfloat))
    print('Total        $ ' + format(total, myfloat))
    print(line)
    print(str(datetime.datetime.now()))

############## call on main program to execute ##############
main()
















          
