

#Sample input:

#Enter name: Lim Ah Seng
#Enter number of hours worked weekly: 10
#Enter hourly pay rate: 6.75
#Enter CPF contribution rate(%): 20

#Sample output:

#Payroll statement for Lim Ah Seng
#Number of hours worked in week: 10
#Hourly pay rate: $6.75
#Gross pay = $67.50
#CPF contribution at 20% = $13.50
#Net pay = $54.00

name = str(input("Enter Name Here:"))
hrs = float(input("Enter Number of Hours Worked Weekly Here:"))
rate = float(input("Enter Hourly Pay Rate Here:"))
cpf = float(input("Enter CPF Contribution Rate Here:"))
print("Payroll statement for " + name)
print("Number of hours worked in week: " + "{0}".format(hrs))
print("Hourly pay rate: $" + "{0:.2f}".format(rate))
gross = hrs*rate
print("Gross pay = $" + "{0:.2f}".format(gross))
cpf20 = gross/5
print("CPF contribution at 20% = $" + "{0:.2f}".format(cpf20))
net = gross-cpf20
print("Net pay = $" + "{0:.2f}".float(net))
