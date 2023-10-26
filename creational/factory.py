from abc import ABCMeta, abstractmethod


class Plugin(metaclass=ABCMeta):
    @abstractmethod
    def type():
        raise NotImplementedError
    

class FilterPlugin(Plugin):
    def __init__(self):
        self.type = 'Filter'

    def type(self):
        return self.type


class ShadowPlugin(Plugin):
    def __init__(self):
        self.type = 'Shadow'

    def type(self):
        return self.type

class Creator:
    @staticmethod
    def Factory(type):
        if type == 'Filter':
            return FilterPlugin()
        elif type == 'Shadow':
            return ShadowPlugin()
        return None
