from tkinter import *
from structural.decorator import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Decorator')
        self.geometry('640x480')
        self.dry = Entity('picture')

        l = Label(self, bg='white', width=30, text=self.dry.run())
        l.pack()
        
        def result():
            if (effOne.get()) and (not effTwo.get()):
                wet = EffectOne(self.dry)
                l.config(text=wet.run())
            elif (not effOne.get()) and (effTwo.get()):
                wet = EffectTwo(self.dry)
                l.config(text=wet.run())
            elif (effOne.get()) and (effTwo.get()):
                wet = EffectOne(EffectTwo(self.dry))
                l.config(text=wet.run())
            else:
                l.config(text=self.dry.run())
        
        effOne = IntVar(value=0)
        effTwo = IntVar(value=0)
        first = Checkbutton(self, text='EffectOne',variable=effOne, command=result)
        first.pack()
        second = Checkbutton(self, text='EffectTwo',variable=effTwo, command=result)
        second.pack()
