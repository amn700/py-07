import ex1


def main() -> None:
    print("Testing Creature with healing capability")
    heal_factory = ex1.HealingCreatureFactory()

    base = heal_factory.create_base()
    evolved = heal_factory.create_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.heal("itself"))

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal("itself"))

    print("Testing Creature with transform capability")
    trans_factory = ex1.TransformCreatureFactory()

    base = trans_factory.create_base()
    evolved = trans_factory.create_evolved()

    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    main()
