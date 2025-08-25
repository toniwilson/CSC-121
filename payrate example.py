# get pay rate and hours worked
pay_rate = float(input("Enter pay rate: "))
hours_worked = float(input("Enter hours worked: "))

# evaluate overtime
if hours_worked > 40:
    # number of overtime hours
    overtime_hours = hours_worked - 40
    # calculate amount for overtime hours
    over_pay = pay_rate * 1.5 * overtime_hours
    
else:
    over_pay = 0
    overtime_hours = 0
    
# calculate gross pay and display results
gross_pay = over_pay + hours_worked * pay_rate
print ()