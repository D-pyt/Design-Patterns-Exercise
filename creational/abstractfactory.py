class FiltersFactory:
    def __init__(self):
        self._filtersfactory = [AddNoise(3, 'noise'), Blur(7, 'blur'), Liquify(24, 'liquify')]

    @property
    def fltrs(self):
        return self._filtersfactory
    

class Filters:
    def __init__(self, parameter, name):
        self.parameter = parameter
        self.name = name

class AddNoise(Filters):
    def __init__(self, parameter, name):
        super().__init__(parameter, name)

    def getParameter(self):
        return super().getParameter()

class Blur(Filters):
    def __init__(self, parameter, name):
        super().__init__(parameter, name)

    def getParameter(self):
        return super().getParameter()
    
class Liquify(Filters):
    def __init__(self, parameter, name):
        super().__init__(parameter, name)

    def getParameter(self):
        return super().getParameter()
  