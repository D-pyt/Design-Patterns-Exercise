from tkinter import *
from behavioral.observer import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Observer')
        self.geometry('640x480')

        self.bluring = Blur("bluring")
        self.movement = MovingPicture()

        l = Label(self, text='change value of the %s' % self.movement.name)
        l.pack()

        scale = Scale(self, command= lambda value: self.change_value(int(value)), from_=0, to=100)
        scale.pack()

    def change_value(self, value):
        self.bluring.attach(self.movement)
        self.bluring.setValue = value
