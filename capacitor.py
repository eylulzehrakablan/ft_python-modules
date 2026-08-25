import ex1


def test_healing(factory: ex1.HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal(), end="\n\n")


def test_transforming(factory: ex1.TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    healing_factory = ex1.HealingCreatureFactory()
    test_healing(healing_factory)

    transform_factory = ex1.TransformCreatureFactory()
    test_transforming(transform_factory)
