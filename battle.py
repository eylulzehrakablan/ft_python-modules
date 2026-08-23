import ex0

def test_factory(factory: ex0.CreatureFactory) -> None:
    print("Testing factory")
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print(base_creature.describe())
    print(base_creature.attack())

    print(evolved_creature.describe())
    print(evolved_creature.attack(), end="\n\n")

def test_battle(factory1: ex0.CreatureFactory, factory2: ex0.CreatureFactory) -> None:
    print("Testing battle")
    fighter1 = factory1.create_base()
    fighter2 = factory2.create_base()

    print(fighter1.describe())
    print(" vs.")
    print(fighter2.describe())
    print(" fight!")
    print(fighter1.attack())
    print(fighter2.attack())


if __name__ == "__main__":
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)

    test_battle(flame_factory, aqua_factory)
