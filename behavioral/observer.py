class Observable:
    def __init__(self):
        self.observers = []

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)


class Blur(Observable):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._amount = 0

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def setValue(self, value):
        self._amount = value
        self.notify()
        

class MovingPicture:
    def __init__(self):
        self._name = "Movement"

    def update(self, subject):
        print('Movement: %s has value %d' % (subject.name, subject.setValue))

    @property
    def name(self):
        return self._name
