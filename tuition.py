import datetime
# define tuition & fee rates
RATE_TUITION_IN = 156.71
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#define global variables
inout = 1
numcredits = 0 
scholarshipamt = 0

tuition = 0
institution_fee = 0
stu_act_fee = 0
cap_fee = 0
total = 0
balance = 0


################# define program functions ######################
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to calculate tuition & fees for another student? ")
        if yesno == "n" or yesno == "N":
            another_student = False
    
def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def perform_calculations():
    global institution_fee, tuition, cap_fee, stu_act_fee, total, balance, numcredits
    if inout == 1:
        tuition = RATE_TUITION_IN * numcredits
        cap_fee = 0
    else:
        tuition = RATE_TUITION_OUT * numcredits
        cap_fee = RATE_CAPITAL_FEE * numcredits
    
    institution_fee = RATE_INSTITUTION_FEE * numcredits
    stu_act_fee = RATE_ACTIVITY_FEE * numcredits
    total = tuition + institution_fee + stu_act_fee + cap_fee
    balance = total - scholarshipamt
    


def display_results():
    moneyf = '10,.2f'
    line=('---------------------------------------------------------------')

    print('\n************* Piedmont Virginia Community College *************')
    print('                Tuition and Scholarship Report')
    print(line)
    print('\tTuition Fee               $ ' + format(tuition,moneyf))
    print('\tInstitutional Fee         $ ' + format(institution_fee,moneyf))
    print('\tStudent Activity Fee      $ ' + format(stu_act_fee,moneyf))
    print('\tCapital Fee               $ ' + format(cap_fee,moneyf))
    print('\tScholarship Amount        $ ' + format(scholarshipamt,moneyf))
    print('\tTotal                     $ ' + format(total,moneyf))
    print('\t\tBALANCE           $ ' + format(balance,moneyf))
    print(line)
    print('\t'+str(datetime.datetime.now()))
    

################### call on main program to execute ################
main()
