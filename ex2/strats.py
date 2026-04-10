import abc
import typing

from ex1.capabilities import HealCapability, TransformCapability


class InvalidCreatureForStrategy(Exception):
    pass


class _Attackable(typing.Protocol):
    def attack(self) -> str: ...


class _TransformingCreature(_Attackable, typing.Protocol):
    def transform(self) -> str: ...

    def revert(self) -> str: ...


class _HealingCreature(_Attackable, typing.Protocol):
    def heal(self, target: object) -> str: ...


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
        attackable = typing.cast(_Attackable, creature)
        print(attackable.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: object) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: object) -> None:
        if not self.is_valid(creature):
            creature_name = creature.__class__.__name__
            raise InvalidCreatureForStrategy(
                f"Invalid Creature '{creature_name}' \
for this aggressive strategy"
            )

        transforming = typing.cast(_TransformingCreature, creature)
        print(transforming.transform())
        print(transforming.attack())
        print(transforming.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: object) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: object) -> None:
        if not self.is_valid(creature):
            creature_name = creature.__class__.__name__
            raise InvalidCreatureForStrategy(
                f"Invalid Creature '{creature_name}' \
for this defensive strategy"
            )

        healing = typing.cast(_HealingCreature, creature)
        print(healing.attack())
        print(healing.heal(healing))
