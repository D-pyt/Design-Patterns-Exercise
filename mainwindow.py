from tkinter import *
from creational.singleton import Singleton
import filterswindow
import factorywindow
import adapterwindow
import decoratorwindow
import facadewindow
import iteratorwindow


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

        self.button = Button(self, text = 'decorator window', command=self.create_decorator)
        self.button.pack(expand=True)

        self.button = Button(self, text = 'facade window', command=self.create_facade)
        self.button.pack(expand=True)

        self.button = Button(self, text = 'Iterator-search', command=self.create_iterator)
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

    def create_decorator(self):
        global extraWindow 
        extraWindow = decoratorwindow.Extra()

    def create_facade(self):
        global extraWindow 
        extraWindow = facadewindow.Extra()

    def create_iterator(self):
        global extraWindow 
        extraWindow = iteratorwindow.Extra()




    def __init__(self):
        print('calling from __init__')
 