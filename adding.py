# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 14:10:02 2025

@author: wilsont1072
"""

emp_num = int(input("Enter number of employees: "))
salaries = open('salaries.txt','a')

for num in range(emp_num):
    print("\nInfo for Employee #", num+1)
    print()
    # get the name and salary for employees
    name = input("Enter Employee Name: ")
    salary = float(input("Enter "+name+"'s salary: $"))
    
    print(f'{name:<15}{salary}'+'\n', file = salaries)
    
salaries.close()