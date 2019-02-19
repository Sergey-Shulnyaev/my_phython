# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:56:38 2019

"""

def element(a,b):
    if a >= b:
        return a
    else:
        return b 

a = int(input('Введите первое число:\n'))
b = int(input('Введите второе число:\n'))
print('Наибольшее число:',element(a,b))