from tkinter import *
from structural.adapter import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Adapter window')
        self.geometry('640x480')

        self.button = Button(self, text = 'RGB', command = self.rgb)
        self.button.pack(expand=True)

        self.button = Button(self, text = 'CMYK', command = self.cmyk)
        self.button.pack(expand=True)

    def rgb(self):
        image = RgbImage()
        image.rgbpicture()

    def cmyk(self):
        image = RgbToCmyk()
        image.rgbpicture()
