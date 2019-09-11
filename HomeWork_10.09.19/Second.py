# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:54:25 2019

@author: mag
"""

import tkinter

class Translater:
    def __init__(self):


        self.main_window = tkinter.Tk()


        self.first_frame= tkinter.Frame()
        self.bottom_frame = tkinter.Frame()


        self.first_string = tkinter.StringVar()
        self.first_label = tkinter.Label(self.first_frame,
                   textvariable=self.first_string)
        self.first_label.pack()



        self.button1 = tkinter.Button(self.bottom_frame,
                                          text='sinister',
                                          command=self.trans1)
        self.button2 = tkinter.Button(self.bottom_frame,
                                          text='dexter',
                                   command=self.trans2)
        self.button3 = tkinter.Button(self.bottom_frame,
                                          text='medium',
                                   command=self.trans3)


        self.button1.pack(side='left')
        self.button2.pack(side='left')
        self.button3.pack(side='left')


        self.first_frame.pack()

        self.bottom_frame.pack()

        tkinter.mainloop()


    def trans1(self):

        self.first_string.set('левый')
    
    def trans2(self):

        self.first_string.set('средний')

    def trans3(self):

        self.first_string.set('правый')


trans = Translater()