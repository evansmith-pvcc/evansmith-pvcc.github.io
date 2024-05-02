# Name: your name here
# Prog Purpose: This program creates a payroll report

import datetime

############## LISTS of data ############
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
     "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

# Calculation lists

gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medicare = []
ret401k = []
net_pay = []

total_gross = 0
total_net = 0

#### TUPLES of constants constants
#             C     S      J      M
#    indexes  0     1      2      3
PAY_RATE = (16.50, 15.75, 15.75, 19.50)

#           fed state  ss    med   ret
#  indexes   0    1     2     3     4
DED_RATE = (.12, .03, .062, .0145, .04 )

###### define progran functions ##
def main():
    perform_calculations()
    display_results()

def perform_calculations():
    global total_gross, total_net, gross_pay, fed_tax, state_tax, soc_sec, medicare, ret401k, net_pay

    for i in range(num_emps):

    #calculate gross pay
        if job[i] == "C":
            gross = hours[i] * PAY_RATE[0]
        elif job[i] == "S":
            gross = hours[i] * PAY_RATE[1]
        elif job[i] == "J":
            gross = hours[i] * PAY_RATE[2]
        else:
            gross = hours[i] * PAY_RATE[3]

    #calculate deductions
        fed = gross * DED_RATE[0]
        state = gross * DED_RATE[1]
        soc = gross * DED_RATE[2]
        med = gross * DED_RATE[3]
        ret = gross * DED_RATE[4]

    #STUDENTS: calculate other deductions here:

        net = gross - fed - state - soc - med - ret #be sure to subtract the other deductions here

    #add to totals
        total_gross += gross
        total_net += net

    #append amounts to lists
        gross_pay.append(gross)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec.append(soc)
        medicare.append(med)
        ret401k.append(ret)
        net_pay.append(net)
#STUDENTS: append other deductions and net pay here:

def display_results():
    currency = '8,.2f'
    line = "-" * 46
    tab = "    "

    print(line)
    print(' ************ FRESH FOODS MARKET ************ ')
    print(' ----------- WEEKLY PAYROLL REPORT ---------- ')
    print(tab + str(datetime.datetime.now()))
    print(line)
    titles1 = "Emp Name" + tab + tab + "Code" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab +"Soc Sec" + tab + "Medicare" + tab + "401K" + tab + "Net"
    print(titles1 + titles2)
#STUDENTS: Create the missing code to print out employee data, one line at a time
    for i in range(num_emps):
        datai = emp[i] + "  " + job[i] + "  " + format(gross_pay[i], currency) + "   " + format(fed_tax[i], currency) + "        " + format(state_tax[i], currency) + "      " + format(soc_sec[i], currency) + "   " + format(medicare[i], currency) + "   " + format(ret401k[i], currency) + " " + format(net_pay[i], currency)
        print(datai)
    print(line)
    print(" ************ TOTAL GROSS: $" + format(total_gross, currency))
    print(" ************ TOTAL NET : $" + format(total_net, currency))
    print(line)
######### call on main program to execute #########

main()