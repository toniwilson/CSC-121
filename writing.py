# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

stu_scores = ['Chris', 'Susie', 'Jessica']

with open('nested.txt', 'w') as contact_file:
    contact_file.writelines(stu_scores)