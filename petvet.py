# Name: Viktoriia Nemyrova
# Program Purpose: This program finds the cost of pet vaccines & medications for dogs and cats
#
# Note: Pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia
import datetime

############# define global variables #############
# define dog prices
PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48
PR_LEP = 21
PR_LYME = 41
PR_RAB = 25

PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

# define cat prices
PR_FELL = 35
PR_FEL = 30
PR_RAB = 25

PR_ALL = 0

PR_CHEWS_ONESIZE = 8.00

# define global variables

############# define program functions #############
def main():
    more = True
    while more:
        get_user_data()

        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()
        askAgain = input("\nWould you like process another pet (Y/N) ?:")
        if askAgain.upper() == "N" :
            more = False
            print('Thank you for trusting PET CARE MEDS with your pet vaccines and medications.')
def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet name: ")
    pet_type = input("Is this pet a dog(D) or cat (C) ? ")
    pet_weight = int(input("Weight of your pet (in pounds): "))

############# Dog functions #############

def get_dog_data():
    global pet_vax_type, num_chews
    dog1 = "\n** Dog Vaccines: \n\t1.Bordatella \n\t2.Dapp \n\t3.Influenza \n\t4.Leptospirosis"
    dog2 = "\n\t5.Lyme Disease \n\t6.Rabies \n\t7.Full Vaccine Package \n\t8.NONE"
    dogmenu = dog1 + dog2
    pet_vax_type = int(input(dogmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all dogs. ")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N) ?")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heart worm chews would you like to order ? "))

def perform_dog_calculations():
    global vax_cost, chews_cost, total

    #### vaccines

    if pet_vax_type == 1 :
        vax_cost = PR_BORD

    elif pet_vax_type == 2 :
        vax_cost = PR_DAPP

    elif pet_vax_type == 3 :
        vax_cost = PR_FLU

    elif pet_vax_type == 4 :
        vax_cost = PR_LEP

    elif pet_vax_type == 5 :
        vax_cost = PR_LYME

    elif pet_vax_type == 6 :
        vax_cost = PR_RAB

    elif pet_vax_type == 7 :
         PR_ALL = PR_BORD + PR_DAPP + PR_FLU + PR_LEP + PR_LYME + PR_RAB
         vax_cost = .85 * PR_ALL

    else:
        vax_cost = 0

    #### heart worm chews
    if num_chews != 0 :
        if pet_weight < 25:
            chews_cost = num_chews * PR_CHEWS_SMALL

        elif pet_weight > 26 and pet_weight < 50 :
            chews_cost = num_chews * PR_CHEWS_MED
    
        else:
            chews_cost = num_chews * PR_CHEWS_LARGE


    #### find total
    total = vax_cost + chews_cost

            
def display_dog_results():
    moneyf = '8,.2f'
    line=('---------------------------------------------------------------')

    print('\n************* Pet Vaccines & Medications *************')
    print('                     Pet Type - Dog')
    print(line)
    print('Vaccine              $ ' + format(vax_cost,moneyf))
    print('Heartworm            $ ' + format(chews_cost,moneyf))
    print('Total                $ ' + format(total,moneyf))
    print(line)
    print('\t'+str(datetime.datetime.now()))

############# Cat functions #############
def get_cat_data():
    global pet_vax_type, num_chews
    cat1 = "\n** Cat Vaccines: \n\t1.Feline Leukemia \n\t2.Feline Viral Phinotracheitis"
    cat2 = "\n\t3.Rabies \n\t4.Full Vaccine Package \n\t5.NONE"
    
    catmenu = cat1 + cat2
    pet_vax_type = int(input(catmenu + "\n** Enter the vaccine number: "))
    
    print("\nMonthly heart worm prevention medication is recommended for all cats. ")
    heart_yesno = input("Would you like to order monthly feline heartworm medication for " + pet_name + " (Y/N) ?")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heart worm chews would you like to order ? "))

def perform_cat_calculations():
    global vax_cost, chews_cost, total
    if pet_vax_type == 1 :
        vax_cost = PR_FELL

    elif pet_vax_type == 2 :
        vax_cost = PR_FEL

    elif pet_vax_type == 3 :
        vax_cost = PR_RAB

    elif pet_vax_type == 4 :
        PR_ALL = PR_FELL + PR_FEL + PR_RAB
        vax_cost = .90 * PR_ALL

    #### heart worm chews

    if num_chews !=0 :
        chews_cost = num_chews *PR_CHEWS_ONESIZE
    total = vax_cost + chews_cost

def display_cat_results():
    moneyf = '8,.2f'
    line=('---------------------------------------------------------------')

    print('\n************* Pet Vaccines & Medications *************')
    print('                    Pet Type - Cat')
    print(line)
    print('Vaccine              $ ' + format(vax_cost,moneyf))
    print('Heartworm            $ ' + format(chews_cost,moneyf))
    print('Total                $ ' + format(total,moneyf))
    print(line)
    print('\t'+str(datetime.datetime.now()))

main()








            
