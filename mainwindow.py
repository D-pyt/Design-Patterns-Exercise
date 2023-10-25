from tkinter import *
from creational.singleton import Singleton
import filterswindow


class Window(Tk, Singleton):
    def init(self):
        print('calling from __init__')
        super().__init__()

        self.button = Button(self, text = 'open filters window', command=self.create_window_filters)
        self.button.pack(expand=True)

    def create_window_filters(self):
        global extraWindow 
        extraWindow = filterswindow.Extra()

    def __init__(self):
        print('calling from __init__')
 