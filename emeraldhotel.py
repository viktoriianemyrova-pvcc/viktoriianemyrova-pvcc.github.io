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
cust = []
# create output file
outfile = 'emerald-web.html'

def main():

    read_in_cust_file()
    open_outfile()
    perform_calculations()
    create_output_file()


def read_in_cust_file():
    cust_data = open("emerald.csv", "r")
    cust_in = cust_data.readlines()
    cust_data.close()

  #split the data into fields

    for i in cust_in:
        cust.append(i.split(","))

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #F8F7F5; background-image: url(beach.png); color: #9F8D7F;">\n')

def perform_calculations():
    global grand_total
    grand_total = 0


    for i in range(len(cust)):
        if cust[i][2] == "SR":
            subtotal = int(cust[i][3]) * PR_ROOM [0]
        elif cust[i][2]== "DR":
            subtotal = int(cust[i][3]) * PR_ROOM [1]           
        else:
            subtotal = int(cust[i][3]) * PR_ROOM [2]

        sales_tax = subtotal * TAX_RATE[0]
        occup_tax = subtotal * TAX_RATE[1]
        total = subtotal + sales_tax + occup_tax
        grand_total += total
        cust[i].append(subtotal)
        cust[i].append(sales_tax)
        cust[i].append(occup_tax)
        cust[i].append(total)
        
        

def create_output_file():
    global f
    currency = '9,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]


    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "8">'
    sp = " "
    f.write('\n<table border="3"   style ="background-color: #F8F7F5;  font-family: bellefair; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2 style =" text-align:center; "> Emerald Beach Hotel & Resort</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('<h3 style =" text-align:center; ">------ Sales Report ------</h3>\n')
    titles1 = tr + "\nLast " + endtd + " First" + endtd + "Type " +  endtd + "Num Nights" +  endtd
    titles2 = "Subtotal" + endtd + "Sales Tax"+ endtd + " Occ. Tax"+ endtd +" Total" + endtr
    f.write(titles1 + titles2)
    
    for i in range(len(cust)):
        data1 = "\n" +tr + cust[i][0]+endtd + cust[i][1]+ endtd + cust[i][2]+ endtd + str(cust[i][3])+ endtd + format(cust[i][4], currency)+ endtd + format(cust[i][5], currency)+ endtd + format(cust[i][6], currency)+endtd + format(cust[i][7], currency)+endtr
        f.write(data1)
        
    f.write( '<tr><td colspan= "7">' + 'Grand Total: '+ endtd + format(grand_total,currency)+ endtr)
    f.write( '<tr><td colspan= "7">' + 'Date/Time: '+ endtd + day_time + endtr)
    
    f.write('</table><br />')
    f.write('</body></html>')
    f.close()
    print('\n** Open this file in a browser window to see your results: ' + outfile)
    

main()

        
        





