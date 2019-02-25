# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:53:33 2019

"""

def str_n(s,n):
    if len(s) > n:
        return s.upper()
    else:
        return s

print('\n',str_n(input('Введите строку:\n'),int(input('Введите n:\n'))))