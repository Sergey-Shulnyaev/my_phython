# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:50:12 2019

@author: mag
"""
import random

class Сustomer():
    def __init__(self, name, address, phoneNumber, money, car):
        self.__name = name
        self.__address = address
        self.__phoneNumber = phoneNumber
        self.__money = money
        self.__car = car

        
        

    
class Сar():
    
    def __init__(self, brandList, modelDict, breakageDict, year = None):
        
        self.__brand = brandList[random.randint(0,len(brandList)-1)] 
        self.__model = list(modelDict.keys())[random.randint(0,len(modelDict)-1)]
        if year == None:
            self.__year = 2019 - random.randint(0,40)
        self.__breakage = list(breakageDict.keys())[random.randint(0,len(breakageDict)-1)]
        
#class Сompany():
#    def __init__(self, money):
        
        
    
brandList = ('Mercedes','Porsche','BMW')
modelDict = {"Седан" : 1, "Универсал" : 1.1, "Микроавтобус" : 1.5, "Минивэн" : 1.3, "Лимузин" : 1.9}  
breakageDict= {"Диагностика автомобиля" : 500, "Ходовая часть" : 15000, "Развал схождения" : 2000,
               "Рулевого управление" : 10000, "Замена масла" : 1000, "Электрика" : 10000,
               "Двигатель" : 20000, "Тормозные системы" : 6000, "Замена жидкостей и фильтров" : 2000,
               "Стёкла" : 7000, "Система впрыска и зажигания" : 4000, "Выхлопная система" : 2000, "Шиномонтаж" : 4765}    
client = Customer("Петров Пётр Петрович", "г. Саратов, Провиантская ул., д. 11, кв. 45", "+71000000000",
                 80000, Car(brandList, modelDict, breakageDict))
