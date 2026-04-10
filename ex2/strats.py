import abc

from ex1.capabilities import HealCapability, TransformCapability

class InvalidCreatureForStrategy(Exception):
    pass
class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def act(self, creature: object) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def is_valid(self, creature: object) -> bool:
        raise NotImplementedError


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: object) -> bool:
        return True

    def act(self, creature: object) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: object) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: object) -> None:
        if not self.is_valid(creature):
            creature_name = creature.__class__.__name__
            raise InvalidCreatureForStrategy(
                f"Invalid Creature '{creature_name}' for this aggressive strategy"
            )

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: object) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: object) -> None:
        if not self.is_valid(creature):
            creature_name = creature.__class__.__name__
            raise InvalidCreatureForStrategy(
                f"Invalid Creature '{creature_name}' for this defensive strategy"
            )

        print(creature.attack())
        print(creature.heal(creature))