from tkinter import *
from tkinter.messagebox import askquestion
from structural.facade import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Facade')
        self.geometry('220x480')

        self.button = Button(self, text='Start creating', command=self.start_creating)
        self.button.pack(expand=True)

    def start_creating(self):
        createImage = CreateImage()
        result = askquestion("...", message="Start rendering?", icon='info')
        if result == 'yes':
            createImage.startCreating()
        else:
            print('Creation canceled')
