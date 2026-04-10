from ex0.creatures import Creature

from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    TYPE = "Grass"

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self, target) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    TYPE = "Grass/Fairy"

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    TYPE = "Normal"

    def __init__(self):
        super().__init__()
        self.STATE = False

    def attack(self) -> str:
        if not self.STATE:
            return "Shiftling attacks normally."
        return "Shiftling performs a boosted strike!"

    def transform(self) -> str:
        if self.STATE is False:
            self.STATE = True
            return "Shiftling shifts into a sharper form!"
        else:
            return f"{self.name} is already transformed"

    def revert(self) -> str:
        if self.STATE is True:
            self.STATE = False
            return "Shiftling returns to normal."
        return f"{self.name} is already in its normal form"


class Morphagon(Creature, TransformCapability):
    TYPE = "Normal/Dragon"

    def __init__(self):
        super().__init__()
        self.STATE = False

    def attack(self) -> str:
        if not self.STATE:
            return "Morphagon attacks normally."
        return "Morphagon unleashes a devastating morph strike!"

    def transform(self) -> str:
        if self.STATE is False:
            self.STATE = True
            return "Morphagon morphs into a dragonic battle form!"
        else:
            return f"{self.name} is already transformed"

    def revert(self) -> str:
        if self.STATE is True:
            self.STATE = False
            return "Morphagon stabilizes its form."
        return f"{self.name} is already in its normal form"
