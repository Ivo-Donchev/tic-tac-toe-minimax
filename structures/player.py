class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()
