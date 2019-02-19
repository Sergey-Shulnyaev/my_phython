# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:56:38 2019

"""

def element(num):
    if num == 3:
        return 'Li'
    elif num == 25:
        return 'Mn'
    elif num == 80:
        return 'Hg'
    elif num == 17:
        return 'Cl'
    else:
        return 'Ошибка ввода'

print(element(int(input("Введите номер элемента:\n"))))