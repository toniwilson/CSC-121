# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 13:28:33 2025

@author: wilsont1072
"""

name = 'jon'
salary = 3000

# 3 step process
# step 1. create a variable that references a file object
# here we tell the program, the name of the file and how we want to work with it
# the mode defines how we are going to work witht the file (w = write, r = read, a = append)
file = open('practice.txt', 'w')

# step 2. process the info. ex. if writing, use the wrtiing methods
# if one line, call the write() method
# if multiple lines (writelines) method

# CAN ONLY WRITE STRING, no numbers
file.write(name+'\n') # can only pass ONE arguement, MUST be a string
file.write(f'{salary}')

# step 3. close the file
file.close()