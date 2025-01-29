# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:25:11 2025

@author: wilsont1072
"""

score = float(input("Enter score or -1 to terminate: "))
while score != -1:
    
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