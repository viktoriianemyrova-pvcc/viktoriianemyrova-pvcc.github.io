# Name: your-name-here
# Prog Purpose: This program finds the cost of movie tickets, popcorn, & drinks
#   The output is sent to an .html file


import datetime


##############  define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99
PR_POPCORN = 12.99
PR_DRINK = 3.99


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


# create output file
outfile = 'tickets.html'




##############  define program functions ################
def main():
    
    open_outfile()
    more_tickets = True
    
    while more_tickets:
        get_user_data()
        perform_calculations()
        create_output_file()
        
        askAgain = input('\nWould you like to order again (Y or N)?: ' )
        if askAgain.upper() == 'N':
            more_tickets = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global 
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Cinema House Movies </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(wp-cinema.png); color: #f8dd61;">\n')
    
def get_user_data():
    global num_tickets,num_popcorn, num_drinks
    num_tickets = int(input('Number of movie tickets: '))
    num_popcorn = int(input('Number of buckets of popcorn: '))
    num_drinks =  int(input('Number of drinks: '))    


def perform_calculations():
    global cost_tickets, cost_popcorn, cost_drinks, subtotal, sales_tax, total
    cost_tickets = num_tickets * PR_TICKET
    cost_popcorn= num_popcorn * PR_POPCORN
    cost_drinks = num_drinks * PR_DRINK


    subtotal = cost_tickets + cost_popcorn + cost_drinks
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax


def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]


    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "


    f.write('\n<table border="3"   style ="background-color: #47161a;  font-family: arial; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2>CINEMA HOUSE MOVIES</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('*** Your neighborhood movie house ***\n')
    
    f.write(tr + 'Tickets' + endtd + str(num_tickets) + endtd + format(cost_tickets,currency) + endtr)
    f.write(tr + 'Popcorn' + endtd + str(num_popcorn) + endtd + format(cost_popcorn,currency) + endtr)
    f.write(tr + 'Drinks ' + endtd + str(num_drinks) + endtd +  format(cost_drinks,currency)  + endtr)


    f.write(tr + 'Subtotal' +  endtd + sp + endtd + format(subtotal,currency)  + endtr)     
    f.write(tr + 'Sales Tax' + endtd + sp + endtd + format(sales_tax,currency) + endtr)
    f.write(tr + 'TOTAL' +     endtd + sp + endtd + format(total,currency) + endtr)
    
    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')




##########  call on main program to execute ############
main()
