# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

keep_going = 'yes'
while keep_going == 'yes':

    # get score
    score = float(input("Enter score: "))
    
    # check valid score
    while score < 0 or score > 100:
        print ("INVALID SCORE!!! Enter a valid score (0-100) ")
        score = float(input("Enter score again: "))
    
    # determine letter grade
    if score >= 90:
        print ("A")
    elif score >= 80:
        print ("B")
    elif score >= 70:
        print ("C")
    else:
        print("F")
    
    keep_going = input("Do you want to run the program again? (yes/no) ")
