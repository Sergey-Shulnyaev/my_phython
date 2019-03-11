# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:49:50 2019

"""

names = ['John', 'Paul', 'George', 'Ringo']
names = list(filter((lambda x:( 'J' <=x[0] <='P')),names))
print(names)