# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:41:56 2019

"""

import math

l_1 = [2, 4, 9, 16, 25]
new_list_1 = []
for i in l_1:
    new_list_1.append(math.sqrt(i))
print(new_list_1)
new_list_2 = list(map((lambda x: math.sqrt(x)),l_1))
print(new_list_2)
new_list_3 = [math.sqrt(i) for i in l_1]
print(new_list_3)