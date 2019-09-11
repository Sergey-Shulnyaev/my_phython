# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:03:53 2019

@author: mag
"""

import tkinter

class Info:
    def __init__(self):


        self.main_window = tkinter.Tk()


        self.first_frame= tkinter.Frame()
        self.bottom_frame = tkinter.Frame()


        self.first_string = tkinter.StringVar()
        self.first_label = tkinter.Label(self.first_frame,
                   textvariable=self.first_string,justify = tkinter.LEFT)
        self.first_label.pack()



        self.info_button = tkinter.Button(self.bottom_frame,
                                          text='Показать инфо',
                                          command=self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                   command=self.main_window.destroy)


        self.info_button.pack(side='left')
        self.quit_button.pack(side='left')


        self.first_frame.pack()

        self.bottom_frame.pack()

        tkinter.mainloop()


    def show_info(self):

        self.first_string.set('Стивен Маркус\n274 Бейли\nУэйнзвилль, Северная Каролина 27999')


inf = Info()