from tkinter import Toplevel, Button
from creational.abstractfactory import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Filters')
        self.geometry('640x480')
        self.button = Button(self, text = 'Show Filters', command = self.show_filters)
        self.button.pack(expand=True)

    def show_filters(self):
        filtersfactory = FiltersFactory()
        fltrs = filtersfactory.fltrs

        for i in fltrs:
            self.button = Button(self, text=f'{i.name}')
            self.button.pack(expand=True)
