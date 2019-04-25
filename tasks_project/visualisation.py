# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:56:38 2019

@author: Sergey Shulnyaev
"""

import tkinter
import json  

def reader():    
    try:
        with open('task.json','r') as f_obj:
            numbers = json.load(f_obj)
        return numbers
    except Exception as e:
        return e


def writer(numb):      
    try:
        with open('task.json','r') as f_obj:
            numbers = json.load(f_obj)
            numbers.append(numb)      
    except:
        numbers =[numb]
    with open('task.json', 'w') as f_obj:
        json.dump(numbers, f_obj)  

def add_to():
    json = {'name' : task_entry.get(),'category':categ_entry.get(),'time':time_entry.get()}
    writer(json)

def print_tasks():
    works = reader()
    string = ""
    for i in works:
         string = "Задача: "+ i['name'] + " Категория: "+ i['category'] + " Дата: " + i['time']
         tasks.insert(END, string)      

color = "#F5F0F0"

window = tkinter.Tk()
window.title('Менеджер задач')

frame=tkinter.Frame(window,bg = color)
frame.grid()




task = tkinter.Label(frame,text = 'Задача:',bg = color)
task.grid(row = 0, column = 0)

task_entry=tkinter.Entry(frame)
task_entry.grid(row = 0, column = 1, columnspan = 2)

category = tkinter.Label(frame,text = 'Категория:',bg = color)
category.grid(row = 1, column = 0)

categ_entry=tkinter.Entry(frame)
categ_entry.grid(row = 1, column = 1, columnspan = 2)


time = tkinter.Label(frame,text = 'Время:',bg = color)
time.grid(row = 2, column = 0)

time_entry=tkinter.Entry(frame)
time_entry.grid(row = 2, column = 1, columnspan = 2)

f = tkinter.Label(frame,text = "      ",bg = color)
f.grid(row = 0, column = 9,rowspan = 9)

f1 = tkinter.Label(frame,text = "      ",bg = color)
f1.grid(row = 8)

tasks = tkinter.Listbox(frame,bg = 'white', width  = 60)
tasks.grid(row = 0, column = 4,columnspan=4,rowspan = 8)
 
add_button = tkinter.Button(frame, text='Добавить',font=('Courier', 10, 'bold'),command = add_to)
add_button.grid(row = 4, column = 1)

list_button = tkinter.Button(frame, text='Список задач',command = print_tasks)
list_button.grid(row = 5, column = 1)


exit_button = tkinter.Button(frame, text='Выход',command=window.destroy)
exit_button.grid(row = 6, column = 1)

window.mainloop()
