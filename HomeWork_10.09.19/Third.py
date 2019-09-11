
import tkinter

class GaloConverter:
    def __init__(self):

        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать три рамки, чтобы сгруппировать элементы интерфейса.
        self.top_frame = tkinter.Frame()
        self.mid1_frame = tkinter.Frame()
        self.mid2_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()


        self.galo_label = tkinter.Label(self.top_frame,
                    text='Введите количество галлонов:')
        self.galo_entry = tkinter.Entry(self.top_frame,
                                        width=10)


        self.galo_label.pack(side='left')
        self.galo_entry.pack(side='left')
        
        self.mile_label = tkinter.Label(self.mid1_frame,
                    text='Введите количество миль:')
        self.mile_entry = tkinter.Entry(self.mid1_frame,
                                        width=20)
        self.mile_label.pack(side='left')
        self.mile_entry.pack(side='left')

        self.descr_label = tkinter.Label(self.mid2_frame,
                   text='Мили на галлон (MPG):')
        self.value = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mid2_frame,
                   textvariable=self.value)


        self.descr_label.pack(side='left')
        self.mpg_label.pack(side='left')


        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Преобразовать',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                   command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')


        self.mid1_frame.pack()
        self.top_frame.pack()
        self.mid2_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()



    def convert(self):

        galo = float(self.galo_entry.get())
        miles = float(self.mile_entry.get())
        MPG = miles / galo

        self.value.set(MPG)

# Создать экземпляр класса KiloConverterGUI.
Galo = GaloConverter()