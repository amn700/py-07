import typing

import ex1


class _CreatureLike(typing.Protocol):
    def describe(self) -> str: ...

    def attack(self) -> str: ...


class _HealingCreature(_CreatureLike, typing.Protocol):
    def heal(self, target: object) -> str: ...


class _TransformingCreature(_CreatureLike, typing.Protocol):
    def transform(self) -> str: ...

    def revert(self) -> str: ...


def main() -> None:
    print("Testing Creature with healing capability")
    heal_factory = ex1.HealingCreatureFactory()

    base_heal = typing.cast(_HealingCreature, heal_factory.create_base())
    evolved_heal = typing.cast(_HealingCreature, heal_factory.create_evolved())

    print("base:")
    print(base_heal.describe())
    print(base_heal.attack())
    print(base_heal.heal("itself"))

    print("evolved:")
    print(evolved_heal.describe())
    print(evolved_heal.attack())
    print(evolved_heal.heal("itself"))

    print("Testing Creature with transform capability")
    trans_factory = ex1.TransformCreatureFactory()

    base_trans = typing.cast(_TransformingCreature,
                             trans_factory.create_base())
    evolved_trans = typing.cast(_TransformingCreature,
                                trans_factory.create_evolved())

    print("base:")
    print(base_trans.describe())
    print(base_trans.attack())
    print(base_trans.transform())
    print(base_trans.attack())
    print(base_trans.revert())

    print("evolved:")
    print(evolved_trans.describe())
    print(evolved_trans.attack())
    print(evolved_trans.transform())
    print(evolved_trans.attack())
    print(evolved_trans.revert())


if __name__ == "__main__":
    main()
