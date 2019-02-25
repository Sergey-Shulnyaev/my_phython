# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:17:48 2019

"""

import math

def num_pi(x):
    return f'{math.pi:.{x}f}'

print(num_pi(int(input('Введите число цифр после запятой для числа Пи:\t'))))