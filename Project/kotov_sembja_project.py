from tkinter import *
import csv
from mini_project import *

def solve0():
    output_label.config(text=solve(var.get()))
    return None

def sww():
    save(var.get(),save_option.get())
    return None

def create_file_window():
    window2 = Tk()
    frame2=Frame(window2, borderwidth=4, relief=GROOVE)
    frame2.grid()
    with open('output.txt',encoding='cp1251') as csvfile:
        csv_read = csv.reader(csvfile)
        lines=[]
        for line in csv_read:
            lines+=line
        file_listbox=Listbox(frame2)
        for line in lines:
            file_listbox.insert(END, line)
  
        file_listbox.grid()


        exit_button2 = Button(frame2, text='Выход.', command=window2.destroy) 
        exit_button2.grid(row=1,column=0,columnspan=1)

        window2.mainloop()
    

window = Tk()

options=["Текст","HTML"]
save_option = StringVar()
save_option.set(options[0])

frame = Frame(window, borderwidth=4, relief=GROOVE)
frame.grid()

title_label=Label(frame,text='Программа для вычисления объёма сферы.')
title_label.grid(row=0,column=0,columnspan=2)

input_title_label=Label(frame,text='Введите радиус:')
input_title_label.grid(row=1,column=0,sticky="w")

var = StringVar()

entry = Entry(frame, textvariable=var)
entry.grid(row=1,column=1,sticky="e")

output_title_label=Label(frame,text='Результат вычислений:')
output_title_label.grid(row=2,column=0,sticky="w")

output_label = Label(frame,text="")
output_label.grid(row=2,column=1)


solve_button = Button(frame, text='Вычислить.', command=solve0) 
solve_button.grid(row=3,column=0,columnspan=2)


save_menu=OptionMenu(frame,save_option, *options)
save_menu.grid(row=4,column=1,sticky="e")

file_button = Button(frame, text='Работа с файлом.', command=create_file_window) 
file_button.grid(row=5,column=0,columnspan=2)

save_button=Button(frame, text='Сохранить.', command=sww)
save_button.grid(row=4,column=0,sticky="w")

exit_button = Button(frame, text='Выход.', command=window.destroy) 
exit_button.grid(row=6,column=0,columnspan=2)

window.mainloop()
