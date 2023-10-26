from pathlib import Path


class RgbCreate:
    def create(self):
        print("creating rgb")
        Path('filename.rgb').touch()

class CmykCreate:
    def create(self):
        print("creating cmyk")
        Path('filename.cmyk').touch()

class CreateImage:
    def __init__(self):
        self.rgb = RgbCreate()
        self.cmyk = CmykCreate()

    def startCreating(self):
        self.rgb.create()
        self.cmyk.create()
