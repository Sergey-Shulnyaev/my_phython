# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:42:59 2019

@author: Lord
"""
# number_reader.py
def reader(filename):
    '''
    Чтение содержимого json файла 
    '''
    import json    
    try:
        with open(filename) as f_obj:
            numbers = json.load(f_obj)
        return numbers
    except Exception as e:
        return e

# number_writer.py
def writer(filename, numbers):    
    import json    
    try:
        with open(filename, 'w') as f_obj:
            json.dump(numbers, f_obj)
    except Exception as e:
        print(e)
        
        
        
print(reader("task.json"))
