class Entity:
    def __init__(self, picture):
        self.picture = picture
 
    def run(self):
        return self.picture
 
class EffectOne(Entity):
    def __init__(self, effOne):
        self.effOne = effOne
 
    def run(self):
        return "EffectOne[{}]".format(self.effOne.run())
 
class EffectTwo(Entity):
    def __init__(self, effTwo):
        self.effTwo = effTwo
 
    def run(self):
        return "EffectTwo[{}]".format(self.effTwo.run())
