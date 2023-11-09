#Name: Carter+Viktoriia 
# Program Purpose: This program computes PVCC college tuition and fees based on number of credits 
# PVCC Fee Rates are from https://www.pvcc.edu/tuition-and-fees

import datetime
#define tax rate #

PERSONAL_TAX=.042
TAX_RELIEF=.33 

#define global variables
cost_vehicle=0
relief_amt=0 
annual_due=0 
biannual_due=0
relief_eligible=0
###### define program function ######
def main ():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results() 
        yesno = input("\nWould you like to calculate the tax owed for another vehicle? (Y or N) " ) 
        if yesno =="n" or yesno=="N":
            another_car= False
            print( " Personal Propert Tax Due by: December 5 2023!")

def get_user_data():
    global cost_vehicle, relief_amt, relief_eligible, annual_due
    cost_vehicle= int(input("What is the assesed value of your vehicle?: "))
    relief_eligible= (input(" Do you use this vehicle for commercial purposes? (Y/N) " ))


def perform_calculations():
    global  relief_amt, relief_eligible, annual_due, biannual_due

    annual_due=(cost_vehicle * PERSONAL_TAX) 
    biannual_due=(annual_due / 2 )

  
   
    if relief_eligible.upper()== "N": 
        relief_amt= ( biannual_due * TAX_RELIEF)
    else:
       relief_amt= 0 

    biannual_due= biannual_due - relief_amt
  

def display_results ():
    moneyf="15,.2f"
    line= '-------------------------------------'
    print (line)
    print ('*****  Tax Bill *******')
    print (line) 
    print('Assesed Value       $ ' + format(cost_vehicle,moneyf))
    print('Annual Amount Owed  $ '+ format(annual_due,moneyf))
    print('Relief Awarded      $ '+ format(relief_amt,moneyf))
    print('Ammount Due Now     $ '+ format(biannual_due,moneyf))
    print(str(datetime.datetime.now()))
   
main()

