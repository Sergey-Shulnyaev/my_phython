# Эта программа демонстрирует группу элементов Radiobutton.
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()


        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
 

        self.radio_var = tkinter.IntVar()
 

        self.radio_var.set(10)

        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Дневное время(6:00 - 17:59)',
                                       variable=self.radio_var,
                                       value=10)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Вечернее время(18:00 - 23:59)',
                                       variable=self.radio_var,
                                       value=12)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Непиковый период(0:00 - 5:59)',
                                       variable=self.radio_var,
                                       value=5)


        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.energy_label = tkinter.Label(self.mid_frame,
                    text='Введите количество минут:')
        self.energy_enter = tkinter.Entry(self.mid_frame,
                                        width=20)
        self.energy_label.pack(side='left')
        self.energy_enter.pack(side='left')
        
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.solve)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                command=self.main_window.destroy)

        
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')


        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
 
        
        tkinter.mainloop()

    # Метод show_choice является функцией обратного вызова
    # для кнопки OK.
    def solve(self):
        tkinter.messagebox.showinfo('Общая стоимость','Ваши затраты = $' + str(float(self.energy_enter.get())* self.radio_var.get() / 100))

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()
