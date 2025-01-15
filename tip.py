# Get the bill amount and tip precentage

bill = float(input("Enter the bill amount $"))
tipPer = float(input("Enter tip percentage (0.15 for 15%): "))

# if < 15%, apply 20%

if tipPer < 0.15 :
    tipPer = 0.20
    print("Tip entered is below 15%!!! therefore 20% tip is applied")

# Calculate tip and total

tip = bill * tipPer
total = bill + tip

# Show result

print("Total to be paid $", round(total,2), sep='')
