'''
# Get the score

score = float(input("Enter the score: "))

# Evaluate score

if score >= 90:
    # get A
    print("A")
elif score >= 80:
    # get B
    print("B")
elif score >= 70:
    # get C
    print("C")
else:

    print("F")

'''

# get the salary

salary = float(input("Enter salary: "))

# evaluate salary

if salary >= 30_000:
    # ask for # of years
    years = int(input("Enter years worked: "))

    if years >= 2:
        # if true, they get the loan
        print("Qualified!! You get the loan")

    else :
        print("Not approved")
        print("Haven't worked for two years or more")

else:
    print("Not approved")
    print("You don't make 30000 or more")
