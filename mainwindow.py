from tkinter import *
from creational.singleton import Singleton
import filterswindow
import factorywindow
import adapterwindow


class Window(Tk, Singleton):
    def init(self):
        print('calling from __init__')
        super().__init__()

        self.button = Button(self, text = 'open filters window', command=self.create_window_filters)
        self.button.pack(expand=True)

        self.button = Button(self, text = 'factory window', command=self.create_factory_filters)
        self.button.pack(expand=True)

        self.button = Button(self, text = 'adapter window', command=self.create_adapter)
        self.button.pack(expand=True)

    def create_window_filters(self):
        global extraWindow 
        extraWindow = filterswindow.Extra()

    def create_factory_filters(self):
        global extraWindow 
        extraWindow = factorywindow.Extra()

    def create_adapter(self):
        global extraWindow 
        extraWindow = adapterwindow.Extra()




    def __init__(self):
        print('calling from __init__')
 