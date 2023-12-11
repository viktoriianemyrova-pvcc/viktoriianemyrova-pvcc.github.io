# Name: Viktoriia Nemyrova
# Prog Purpose: This program is a sales report.
#   The output is sent to an .html file

import datetime

##############  define global variables ############

#           s-tax   occ-tax
#             0       1
TAX_RATE = (.065, .1125,)

#           SR   Dr  SU
#           0    1    2
PR_ROOM = (195, 250, 350)
# define global variables
num_nights = 0


cost_sr_room = 0
cost_dr_room = 0
cost_su_room = 0


subtotal = 0
sales_tax = 0
occup_tax = 0
total = 0
grand_total = 0

# create output file
outfile = 'emerald.html'

def main():

    read_in_cust_file()
    open_outfile()
    get_user_data()
    perform_calculations()
   # create_output_file()


def read_in_cust_file():
    cust_data = open("emerald.csv", "r")
    cust_in = cust_data.readlines()
    cust_data.close()

  #split the data into fields
    cust = []
    for i in cust_in:
        cust.append(i.split(","))
    print(cust)

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #F8F7F5; background-image: url(beach.png); color: #9F8D7F;">\n')

def perform_calculations():


   for i in range(cust):
       print(i)
       

  
        

def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]


    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "


    f.write('\n<table border="3"   style ="background-color: #F8F7F5;  font-family: bellefair; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2> Emerald Beach Hotel & Resort</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('*** Sales Report***\n')

    f.write(tr + 'Tickets' + endtd + str(num_tickets) + endtd + format(cost_tickets,currency) + endtr)
    f.write(tr + 'Popcorn' + endtd + str(num_popcorn) + endtd + format(cost_popcorn,currency) + endtr)
    f.write(tr + 'Drinks ' + endtd + str(num_drinks) + endtd +  format(cost_drinks,currency)  + endtr)


    f.write(tr + 'Subtotal' +  endtd + sp + endtd + format(subtotal,currency)  + endtr)     
    f.write(tr + 'Sales Tax' + endtd + sp + endtd + format(sales_tax,currency) + endtr)
    f.write(tr + 'Occupancy tax rate')
    f.write(tr + 'TOTAL' +     endtd + sp + endtd + format(total,currency) + endtr)
    
    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')
    print('\n** Open this file in a browser window to see your results: ' + outfile)
    f.write('</body></html>')
    f.close()


        
        





