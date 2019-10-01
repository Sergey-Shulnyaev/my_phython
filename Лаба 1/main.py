import tkinter
import datetime
import pygame
from PIL import Image, ImageTk
import tkinter.messagebox

class Clock():
    def __init__(self):

        self.alarmFlag = 0
        self.minute = 0
        self.hour = 0
        self.alarmHour = 9
        self.alarmMinute = 0
        pygame.init()
        pygame.mixer.music.load('minecraftTheme.mp3')
        
        
    def hour_Increment(self):

        if self.alarmFlag == 1:
            self.alarmHour = (self.alarmHour + 1) % 24
        else:
            self.hour = self.hour + 1
        
    def minute_Increment(self):

        
        if self.alarmFlag == 1:
            self.alarmMinute = (self.alarmMinute + 1) % 60
        else:
            self.minute = self.minute + 1
    
    def push_Alarm(self):
        self.alarmFlag = (self.alarmFlag + 1) % 3


    def get_Time(self):
        tm = datetime.datetime.today()
        ti = [i for i in tm.timetuple()][3:6]
        minute = ti[1] + self.minute
        hour = (ti[0] + self.hour + (minute // 60)) % 24
        minute = minute % 60
        
        if self.alarmFlag == 0:
            return [hour, minute, ti[2], self.alarmFlag]
        elif self.alarmFlag == 1:
            return [self.alarmHour, self.alarmMinute, 0, self.alarmFlag]
        elif self.alarmFlag == 2:          
            if self.alarmHour == hour and self.alarmMinute == minute and ti[2] == 0:
                pygame.mixer.music.play()                
                res = tkinter.messagebox.askyesno("Будильник","Перенести будильник на пять минут?")
                if res == 1:
                    self.alarmMinute += 5
                else:
                        self.alarmFlag = 0 
                pygame.mixer.music.stop()

            return [hour, minute, ti[2], self.alarmFlag] 
        
class Main():
    def __init__(self):
        self.window = tkinter.Tk()
        self.frame = tkinter.Frame(self.window)
        self.frame.grid()
        
        self.cl = Clock()
        
        
        self.hour_button = tkinter.Button(self.frame, text = 'H', command = self.cl.hour_Increment)
        self.minute_button = tkinter.Button(self.frame, text = 'M', command = self.cl.minute_Increment)
        self.alarm_button = tkinter.Button(self.frame, text = 'A', command = self.cl.push_Alarm)
        self.exit_button = tkinter.Button(self.frame, text = 'exit', command = self.window.destroy)

        
        self.clock = tkinter.Label(self.frame, text = "{0},{1},{2}".format(self.cl.get_Time()[0], self.cl.get_Time()[1], self.cl.get_Time()[2]) , font = ('fixedsys', 30))
        self.clock.grid(row = 0,column = 0, columnspan = 3)
        
        #Image
        self.red = Image.open("red.jpg")
        self.green = Image.open("green.jpg")
        self.reds = ImageTk.PhotoImage(self.red)
        self.greens = ImageTk.PhotoImage(self.green)
        self.square = tkinter.Label(image = self.reds)
        self.square.image = self.reds
        #self.greenSquare = tkinter.Label(self.frame, image = ImageTk.PhotoImage(self.green))
        #https://pythonbasics.org/tkinter-image/
        self.hour_button.grid(row = 1, column = 0)
        self.minute_button.grid(row = 1, column = 1)
        self.alarm_button.grid(row = 1, column = 2)
        self.exit_button.grid(row = 2, column = 1)
        self.square.grid(row = 2, column = 0)
        
        
        
        self.tick()
        self.window.mainloop()
        
    def tick(self):
        t = self.cl.get_Time()
        s = str(t[0]).zfill(2) + ":"  + str(t[1]).zfill(2) + ":" + str(t[2]).zfill(2)
        self.clock.configure(text = s)
        if t[3] == 2:
            self.square.configure(image = self.greens)
            self.square.image = self.greens
        else:
            self.square.configure(image = self.reds)
            self.square.image = self.reds
        self.clock.after(200, self.tick)
            
            
        


    
mm = Main()  

