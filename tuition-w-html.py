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


# create output file
outfile = 'tuition-webpage.html'


################# define program functions ######################
def main():

    open_outfile()
    more = True
    while more:
        get_user_data()
        perform_calculations()
        create_output_file()
        yesno = input("\nWould you like to calculate tuition & fees for another student? ")
        if yesno == "n" or yesno == "N":
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Piedmont Virginia Community College </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #B26262; background-image: url(wp-tuition.png); color: #000000;">\n')

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
    print(balance)
    
def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]
    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "

    f.write('\n<table border="5"   style ="background-color: #B26262;  font-family: arial; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2> Piedmont Virginia Community College </h2></td></tr>')
    f.write(colsp + '\n')
    f.write(' Tuition and Scholarship Report \n')
    
    f.write(tr + 'Tuition Fee' + endtd + format(tuition,currency) + endtr)
    f.write(tr + 'InstitutionalFee'  + endtd + format(institution_fee,currency) + endtr)
    f.write(tr + 'Student Activity Fee'  + endtd + format(stu_act_fee,currency) + endtr)    
    f.write(tr + 'Capital Fee ' + endtd + format(cap_fee,currency) + endtr)

    f.write(tr + 'Scholarship Amount ' + endtd + format(scholarshipamt,currency)  + endtr)
    f.write(tr + 'Total ' + endtd + format(total,currency)  + endtr)
    f.write(tr + 'BALANCE '+ endtd + format(balance,currency)  + endtr)

    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')

    

    

################### call on main program to execute ################
main()
