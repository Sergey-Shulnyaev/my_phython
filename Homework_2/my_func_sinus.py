# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:11:07 2019

"""
import math

def my_sinus(x):
    if 0.2 <= x <= 0.9:
        return math.sin(x)
    else:
        return 1

x = float(input('Введите угол:\t'))
print('Синус данного угла равен:\t', f'{my_sinus(x):.3f}')