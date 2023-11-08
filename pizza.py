# NAME: DEVIN & VIKTORIIA
# PROG PURPOSE: Pizza Menu and Ordering
####Prices####
# Small pizza   $ 9.99
# Medium        $ 12.99
# Large         $ 17.99
# X Large       $ 21.99
# Drink         $ 3.99
# Bread         $ 6.99
# Sales Tax     5.5% (.055)

import datetime

########### Global Varibales ########
PR_SMALL = 9.99
PR_MED = 12.99
PR_LARGE = 17.99
PR_XLARGE = 21.99
PR_DRINK = 3.99
PR_BREAD = 6.99
SALES_TAX = .055
num_pizza = 0
num_drink = 0
num_stick = 0
pie_cost = 0
pie_total = 0
pie_size = 0
sales_tax = 0
total = 0
subtotal = 0



def main():

    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nIs there another order (Y or N)? ")
        if yesno == "N" or yesno == "n":
            more = False
            print("Thank you for your order! Enjoy your food!")

def get_user_data():
    global num_pizza, pie_size, num_drink, num_stick
    pies = "\n** Pizza Menu\n\t1.Small Pizza         $ 9.99\n\t2.Medium Pizza        $12.99\n\t3.Large Pizza         $17.99\n\t4.Extra Large Pizza   $21.99"
    pie_size = int(input(pies + "\n**What size pizza would you like(1,2,3,or 4)? "))
    num_pizza = int(input("\nHow many pizzas? "))

    num_drink = int(input("\nHow many drinks? $3.99 each. "))
    num_stick = int(input("\nHow many breadsticks? $6.99 each. "))
    
def perform_calculations():
    global total, subtotal, sales_tax, pie_total, drink_total, stick_total

    if pie_size == 1 :
        pie_cost = PR_SMALL

    elif pie_size == 2 :
        pie_cost = PR_MED

    elif pie_size == 3 :
        pie_cost = PR_LARGE

    elif pie_size == 4 :
        pie_cost = PR_XLARGE

    pie_total = pie_cost * num_pizza
    drink_total = num_drink * PR_DRINK
    stick_total = num_stick * PR_BREAD
    subtotal = pie_total + drink_total + stick_total
    sales_tax = subtotal * SALES_TAX
    total = subtotal + sales_tax



def display_results():
    moneyf = '8,.2f'
    line = '--------------------------------'
    print(line)
    print('********Palermo Pizza********')
    print(line)
    print(format(num_pizza) + ' Pizzas ordered')
    print('Pizza(s)        $ ' + format(pie_total,moneyf))
    print('Drinks          $ ' + format(drink_total,moneyf))
    print('Breadsticks     $ ' + format(stick_total,moneyf))
    print(line)
    print('Subtotal        $ ' + format(subtotal,moneyf))
    print('Sales tax       $ ' + format(sales_tax,moneyf))
    print(line)
    print('Total           $ ' + format(total,moneyf))
        
    



main()
