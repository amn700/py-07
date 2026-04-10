import typing

import ex0


class CreatureLike(typing.Protocol):
    def describe(self) -> str: ...

    def attack(self) -> str: ...


class FactoryLike(typing.Protocol):
    def create_base(self) -> CreatureLike: ...

    def create_evolved(self) -> CreatureLike: ...


def test_factory(factory: FactoryLike) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(flame_factory: FactoryLike, aqua_factory: FactoryLike) -> None:
    print("Testing battle")
    flame = flame_factory.create_base()
    aqua = aqua_factory.create_base()

    print(flame.describe())
    print("vs.")
    print(aqua.describe())
    print("fight!")
    print(flame.attack())
    print(aqua.attack())


def main() -> None:
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()

    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    print()
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
