from abc import ABC, abstractmethod

class RGB(ABC):
    @abstractmethod
    def rgbpicture():
        pass

class CMYK(ABC):
    @abstractmethod
    def cmykImage():
        pass

class RgbImage(RGB):   
    def rgbpicture(self):
        print("RGB here")

class CmykImage(CMYK):  
    def cmykImage(self):
        print("CMYK here")
        
class RgbToCmyk(RGB): 
    def __init__(self):
        self.cmyk = CmykImage()
        
    def rgbpicture(self):
        self.cmyk.cmykImage()
