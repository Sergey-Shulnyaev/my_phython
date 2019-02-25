# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:34:36 2019

"""

s = 'У лукоморья 123 дуб зеленый 456'
a = s.find('я')
if a != -1:
    print('Индекс буквы "я":\t',a)
print('Число повторений буквы "у":\t', s.count('у'))
if s.isalpha() == False:
    print(s.upper())
if len(s) > 4:
    print(s.lower())
print('О'+s[1:])