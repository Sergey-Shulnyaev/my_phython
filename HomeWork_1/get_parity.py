# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:17:18 2019

"""
def chetn(num):
    if num % 2 == 0:
        return 'чётное'
    else:
        return 'нечётное'

a = int(input('Введите число:\n'))
print('Число', chetn(a))