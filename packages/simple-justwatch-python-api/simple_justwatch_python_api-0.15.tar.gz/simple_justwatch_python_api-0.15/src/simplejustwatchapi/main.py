from itertools import product

from justwatch import details, offers_for_countries, search


from dataclasses import dataclass


@dataclass
class Base:
    base_field_1: int
    base_field_2: int


@dataclass
class Child(Base):
    child_field_1: int


def main():
    obj = Child(1, 2, 3)
    # result = details("ts4")  # Breaking Bad
    # result = details("tss25")  # Breaking Bad S5
    # result = details("tse411")  # Breaking Bad S5E1
    # result = details("tm10")  # The Matrix
    result = details("ts20711")  # The Simpsons
    # result = search("The Simpsons")
    print(result)
    print()


if __name__ == "__main__":
    main()
