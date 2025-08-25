# get starting value and ending limit
keep_going = 'y'

while keep_going == 'y':

    pay_rate = int(input("Enter pay rate: "))
    hours = int(input("Enter hours worked: "))
    
    while hours < 0 : 
        # not good
        print ('Invalid anser! Must be a positive number')
        hours = int(input("Enter hours worked: "))
        
    gross_pay = pay_rate * hours
    print(gross_pay)
    
    keep_going = input("Do you want to run the program again? (y for yes) ")
    
'''

What not to do: 
    
(stop = True
while stop: 

or 
    
while True:)
    pay_rate = int(input("Enter pay rate: "))
    hours = int(input("Enter hours worked: "))
    
    gross_pay = pay_rate * hours
    print(gross_pay)
    
    keep_going = input("Do you want to run the program again? (y for yes) ")
    
    if keep_going == 'y':
        continue
    else:
        break
'''