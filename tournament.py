import typing

import ex0
import ex1

from ex2.strats import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidCreatureForStrategy,
    NormalStrategy,
)

Opponent = tuple[typing.Any, BattleStrategy]


def _strategy_label(strategy: BattleStrategy) -> str:
    name = strategy.__class__.__name__
    return name.removesuffix("Strategy")


def _factory_label(factory: typing.Any) -> str:
    name = factory.__class__.__name__
    if "Healing" in name:
        return "Healing"
    if "Transform" in name:
        return "Transform"
    try:
        creature = factory.create_base()
        return typing.cast(str, getattr(creature, "name",
                                        creature.__class__.__name__))
    except Exception:
        return name


def _opponents_repr(opponents: list[Opponent]) -> str:
    parts = []
    for f, s in opponents:
        parts.append(f"({_factory_label(f)}+{_strategy_label(s)})")
    return "[ " + ", ".join(parts) + " ]"


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]

            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()

            print("\n* Battle *")
            print(creature_a.describe())
            print("vs.")
            print(creature_b.describe())
            print("now fight!")

            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except InvalidCreatureForStrategy as exc:
                print(f"Battle error, aborting tournament: {exc}")
                return


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    opponents_0: list[Opponent] = [
        (ex0.FlameFactory(), normal),
        (ex1.HealingCreatureFactory(), defensive),
    ]
    print("Tournament 0 (basic)")
    print(_opponents_repr(opponents_0))
    battle(opponents_0)

    opponents_1: list[Opponent] = [
        (ex0.FlameFactory(), aggressive),
        (ex1.HealingCreatureFactory(), defensive),
    ]
    print("\nTournament 1 (error)")
    print(_opponents_repr(opponents_1))
    battle(opponents_1)

    opponents_2: list[Opponent] = [
        (ex0.AquaFactory(), normal),
        (ex1.HealingCreatureFactory(), defensive),
        (ex1.TransformCreatureFactory(), aggressive),
    ]
    print("\nTournament 2 (multiple)")
    print(_opponents_repr(opponents_2))
    battle(opponents_2)


if __name__ == "__main__":
    main()
