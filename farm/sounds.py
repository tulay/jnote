

class Animal:
    def __init__(self, sound):
        self.sound = sound

    def sayit(self, count=4):
        return (self.sound.capitalize() + "! ") * count


class Duck(Animal):
    def __init__(self):
        super().__init__("quack")

