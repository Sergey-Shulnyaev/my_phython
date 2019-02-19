# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:24:25 2019

"""

def func(a):
    if -2.4 <= a <= 5.7:
        return a ** 2
    else:
        return 4

chislo = float(input('Введите вещественное число:\t'))
print(func(chislo))
