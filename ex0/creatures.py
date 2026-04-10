import abc


class Creature(abc.ABC):
    TYPE = "Unknown"

    def __init__(self):
        self.name = self.__class__.__name__
        self.type = self.TYPE

    @abc.abstractmethod
    def attack(self):
        pass

    def describe(self):
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    TYPE = "Fire"

    def attack(self):
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    TYPE = "Fire/Flying"

    def attack(self):
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    TYPE = "Water"

    def attack(self):
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    TYPE = "Water"

    def attack(self):
        return "Torragon uses Hydro Pump!"
