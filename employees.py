# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def main():
    # program gets salaries for num of employees
    # ask the user for the number of employees
    emp_num = int(input("Enter number of employees: "))
    
    # start a loop that gets salary for each employee
    # call an emp_info function
    emp_info(emp_num)
    
def emp_info(employee_num):
    '''
    

    Parameters
    ----------
    employee_num : number of employees

    Returns
    -------
    None.

    '''
    salaries = open('salaries.txt','w')
    
    print(f'{"Name":<15}{"Salary"}')
    
    # salaries.write(f'{"Name":<15}{"Salary"}'+'\n')
    print('-'*25)
    # salaries.write('-'*25+'\n')
    for num in range(employee_num):
        print("\nInfo for Employee #", num+1)
        print()
        # get the name and salary for employees
        name = input("Enter Employee Name: ")
        salary = float(input("Enter "+name+" 's salary: $"))
        salaries.write(f'{"name":<15}{"salary"}'+'\n')

main()