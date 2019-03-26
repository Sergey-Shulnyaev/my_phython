# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:00:38 2019

"""

def calc(a,b,op):
    try:
       if op == '+':
           return a + b
       elif op == '-':
           return a - b
       elif op == '/': 
           return a / b
       elif op == '*':
           return a * b
       elif op == 'выход':
           return '2'
       else:
           return "3"
    except ZeroDivisionError:
        return "1"

           
        
op = 0    
print("Для выхода из калькулятора наберите в оператор 'выход'")
while True:
    a = float(input("Введите первое число:  "))
    b = float(input("Введите второе число:  "))
    op = input("Введите оператор:  ")
    res = calc(a,b,op)
    if res == "1":
        print("Ошибка деления на ноль, попробуйте ещё раз")
    elif res =='2':
        break
    elif res == "3":
        print("Ошибка ввода, попробуйте ещё раз")
    else:
        print("Результат:  ",res)