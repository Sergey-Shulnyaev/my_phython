# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:30:44 2019

"""

cou = 0 
maxx = 0
minn = 200
summ = 0
with open('temper.stat','r') as file:
    templst = file.readlines()
for t in templst:
    temperature = float(t.strip())
    if templst.index(t) == 1:
        cou += 1
    if temperature > maxx:
        maxx = temperature
    if temperature < minn:
        minn = temperature
    summ += temperature


print("Максимальная температура: ",maxx)
print("Минимальная температура: ",minn)
print("Средняя температура: ", summ/len(templst))
print("Количество уникальных температур: ",len(set(templst)))