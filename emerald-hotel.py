#Name: your name here
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195,250,350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065,0.1125)
 
########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = [] 

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
            
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()

    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))
        

def perform_calculations():
    global grandtotal
    grandtotal=0
    
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights
            elif room_type =="DR":
                subtotal = ROOM_RATES[1] * num_nights
            else:
                subtotal = ROOM_RATES[2] * num_nights

#STUDENTS: COMPLETE THESE CALCULATIONS        
            salestax  = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total     = subtotal + salestax + occupancy
             
            grandtotal += total
        
#STUDENTS: ADD THE REST OF THE append statements after this one       
            guest[i].append(subtotal)
            guest[i].append(salestax)
            guest[i].append(occupancy)
            guest[i].append(total)



def open_out_file():        
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style>body {background: url(wp-emerald.jpg)}'
            'table {width: 50%; margin: 50px auto; border-collapse: collapse;} '
            'td, th {border: 1px solid #000000; padding: 8px; text-align: center;} '
            'th {background-color: #4CAF50; color: white;} </style></head>\n')
    f.write('<body>\n')

def create_output_html():
    global f

    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    # HTML table structure setup
    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan="8">'

    f.write('<table border="3" style="background-color: #aedbae; font-family: Arial, sans-serif;">\n')

    f.write(colsp + '<h2>**EMERALD BEACH HOTEL & RESORT**</h2></td></tr>')
    f.write(colsp + 'Guest Financial Report</td></tr>')
    f.write(colsp + 'Date/Time: ' + day_time + endtr)

    # Table headers
    f.write(tr + 'Last Name' + endtd + 'First Name' + endtd + 'Room Type' + endtd + 'Num Nights' + endtd +
            'Subtotal' + endtd + 'Sales Tax' + endtd + 'Occupancy Tax' + endtd + 'Total' + endtr)

    # Table content from guest data
    for data in guest:
        f.write(tr + data[0] + endtd + data[1] + endtd + data[2] + endtd + str(data[3]) + endtd + 
                '$' + format(float(data[4]), currency) + endtd + 
                '$' + format(float(data[5]), currency) + endtd + 
                '$' + format(float(data[6]), currency) + endtd + 
                '$' + format(float(data[7]), currency) + endtr)

    # Grand total
    f.write(colsp + 'Grand Total: ' + '$' + format(grandtotal, currency) + '</td></tr>\n')
    f.write('</table><br />\n')
    f.write('</body></html>')
    f.close()
    print('Open ' + outfile + ' to view the data.')

##call on main program to execute##
main()
