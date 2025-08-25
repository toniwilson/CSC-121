['Tom', 'Jessica', 'Susan']

for name in ['Tom', 'Jessica', 'Susan']:
    print ("Hello")
    print ("Good afternoon", name)
    
print ()
    
for num in [5,6,7,8,9,10]:
    print (num, num*num, num**3)
    
print ()
    
for num in range(10): # starts at 0 & goes up to but not including
    print (num, num*num, num**3)
    
print ()
     
for num in range(5,11): # 5 to 10 (goes up to but not including)
    print (num, num*num, num**3)
    
print ()
    
for num in range (5,26,2): # want to go up in increments of 2
    print (num, num*num, num**3)
    
print ()
    
for num in range (5,26,5): # want to go up in increments of 5
    print (num, num*num, num**3)
    
print ()

for num in range(25, 4, -1): # want the increments to go down by 1
    print (num, num*num, num**3)
    
print ()

for num in range(25, 4, -5): # want the increments to go down by 5
    print (num, num*num, num**3)
    
print ()

# get starting value and ending limit
start = int(input("Enter starting value: "))
end = int(input("Enter ending limit: "))

for num in range(start, end+1):
    print (num, num*num, num**3)

print ()