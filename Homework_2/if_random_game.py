# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:43:30 2019

"""
import random

def Game(a):
    b = random.randint(1,4)
    if a == b:
        return 'Вы победили.'
    elif a < b:
        return 'Ваше число меньше искомого'
    else:
        return 'Ваше число больше искомого'


a = int(input("Компьютер загадал число,\nпопробуйте его угадать:\t"))
print(Game(a))