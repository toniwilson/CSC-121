# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:10:34 2025

@author: wilsont1072
"""

def main():
    # call the welcome function
    welcome()
    
    # call the get_grade function
    get_grade()
    
def welcome():
    '''
    function doesn't require arguements.
    asks user to enter their name and says hi to them.

    '''
    name = input("Enter your name: ")
    print("Hello", name)
    print()
    
def get_grade():
    '''
    asks user to enter score and determines grade

    Returns
    -------
    None.

    '''
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
        
        score = float(input("Enter score or -1 to terminate: "))
    
main()