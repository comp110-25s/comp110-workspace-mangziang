"""My first exercise in COMP110!"""

__author__ = "730484477"


def greet(name: str) -> str:
    """A welcoming first function definiton."""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
