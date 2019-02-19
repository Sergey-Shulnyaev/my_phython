# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:37:06 2019

"""

def vibor_film(film,time):
    if film == 'Пятница':
        if time == 12:
            return 250
        elif time == 16:
            return 350
        elif time == 20:
            return 450
    elif film == 'Чемпионы':
        if time == 10:
            return 250
        elif time == 13:
            return 350
        elif time == 16:
            return 350
    elif film == 'Пернатая банда':
        if time == 10:
            return 350
        elif time == 14:
            return 450
        elif time == 18:
            return 450
    else:
        return 0

def skidka(data,numbil):
    a = 1
    if data == 'Завтра' or data == 'завтра':
        a -= 0.05
    elif data != 'сегодня' or data != 'Сегодня':  
        return 0
    if numbil >= 20:
        a -= 0.2
    return a

film = input('Сейчас в кино фильмы:"Пятница", "Чемпионы", "Пернатая банда"\nВыберите фильм:\t')
data = input('Введите дату сеанса:\t')
time = int(input('Введите время сеанса:\t'))
numbil = int(input('Укажите количество билетов:\t'))
a = vibor_film(film,time) 
b = skidka(data,numbil) * numbil
if a * b == 0:
    print('Ошибка ввода')
else:
    print('Стоимость булетов будет:',a*b)
    