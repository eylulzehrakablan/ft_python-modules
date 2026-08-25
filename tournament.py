import ex0
import ex1
import ex2


def battle(
        opponents: list[tuple[ex0.CreatureFactory, ex2.BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("\n* Battle *")
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except ex2.InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":

    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()
    healing_factory = ex1.HealingCreatureFactory()
    transform_factory = ex1.TransformCreatureFactory()

    normal = ex2.NormalStrategy()
    aggressive = ex2.AggressiveStrategy()
    defensive = ex2.DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flaming+Normal), (Healing+Defensive) ]")
    battle([
        (flame_factory, normal),
        (healing_factory, defensive)
    ])

    print("\nTournament 1 (error)")
    print("[ (Flaming+Aggressive), (Healing+Defensive) ]")
    battle([
        (flame_factory, aggressive),
        (healing_factory, defensive)
    ])

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (aqua_factory, normal),
        (healing_factory, defensive),
        (transform_factory, aggressive)
    ])
