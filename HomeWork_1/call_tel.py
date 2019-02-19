# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:28:42 2019

"""

def stoim(kod, dlit):
    if kod == 343:
        return 15 * dlit
    elif kod == 381:
        return 18 * dlit
    elif kod == 473:
        return 13 * dlit
    elif kod == 485:
        return 11 * dlit
    
kod = int(input('Введите код города:\t'))
vremya = float(input('Введите время звонка:\t'))
print('Стоимость разговора:\t',stoim(kod,vremya),'рублей.')