"""I am Planning a Tea Party With Friends"""

__author__ = "730487744"


def main_planner(guests: int) -> None:
    """Cumulative cost, number of treats and tea bags"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))
    return None


def tea_bags(people: int) -> int:
    """The number of tea bags needed for all the guests"""
    return people * 2


def treats(people: int) -> int:
    """The number of treats needed for everyone at the party"""
    return int((tea_bags(people=people) * 1.5))


def cost(tea_count: int, treat_count: int) -> float:
    """The cost of tea bags and treats combined for a number of guests"""
    return float(tea_count * 0.50 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
