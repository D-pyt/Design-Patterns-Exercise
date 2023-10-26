from tkinter import *
from creational.factory import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Filters factory')
        self.geometry('1280x200')
        self.entry = Entry(self, width=15, textvariable=StringVar())
        self.entry.pack()
        self.button = Button(self, text = 'Drag filters', command = self.show_factory)
        self.button.pack(expand=True)

    def show_factory(self):
        drop = self.entry.get()
        effect = Creator().Factory(drop)

        if effect:
            l = Label(self, text = 'You dropped {}'.format(effect.type))
            l.pack()
