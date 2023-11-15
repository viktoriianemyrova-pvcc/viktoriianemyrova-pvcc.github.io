# Name: Viktoriia Nemyrova
# Program Purpose: This program uses lists to find the personal property tax for vehicles in Charlottesville
#   and produces a report which displays all data and the total tax due
#
# Personal Property tax in Charlottesville:
#       -- $4.20 per $100 of the vehicle value (4.20% per year)
#       -- Paid every six month
# Personal Property Tax Relief (PPTR):
#       -- Eligibility: Owned or leased vehicles which are predominately used for non-business pirposes & have passenger license plates
#       -- Tax relief for qualified vehicles is 33%

import datetime

################# define tax rate #################
PPT_RATE = .042
RELIEF_RATE = .33

################# create list data #################
vehicle = ["2019 Volvo ",
           "2018 Toyota",
           "2022 Kia   ",
           "2020 Ford  ",
           "2023 Honda ",
           "2019 Lexus ",]

vehicle_value = [13000, 10200, 17000, 21000, 28000, 16700,]

pptr_eligible = ["Y", "Y", "N", "Y", "N", "Y", ]

owner_name = ["Brand, Debra      ",
              "Smith, Carter     ",
              "Johnson, Bradley  ",
              "Garcia, Jennifer  ",
              "Henderson, Leticia",
              "White, Danielle   ",]

ppt_owed = []

num_vehicles = len(vehicle)
tax_due = 0
total = 0


################# define program functions #################

def main():
        perform_calculations()
        display_results()

def perform_calculations():
    global total

    for i in range(num_vehicles):

        tax_due = (vehicle_value[i] * PPT_RATE) / 2

        if pptr_eligible[i].upper() == "Y":
            tax_due = tax_due * .67

        ppt_owed.append(tax_due)

        total = total + tax_due

def display_results():
    moneyf = '8,.2f'
    line =("------------------------------------------------------------------------")
    tab = "\t"

    print (line)
    print ("************************ PERSONAL PROPERTY TAX REPORT ************************")
    print ("                          Charlottesville, Virginia")

    print ("\n\t\tRUN DATE/TIME: " + str(datetime.datetime.now()))
    print ("\nNAME" + tab + tab + tab +  "VEHICLE" + tab + tab + "VALUE" + tab + tab + "RELIEF" + tab +" TAX DUE")
    print (line)

    for i in range(num_vehicles):
        dataline1 = owner_name[i]+ tab + vehicle[i] + tab + format(vehicle_value[i],moneyf) + tab
        dataline2 = pptr_eligible[i] + tab + format(ppt_owed[i],moneyf)
        print(dataline1+ dataline2)

    print (line)
    print ("********************************************** TOTAL TAX DUE: " + tab + format(total,moneyf))

main()
   


























        













        
    
















