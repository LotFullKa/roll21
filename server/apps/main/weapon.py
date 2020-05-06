from enum import Enum


class Weapon:

    def __init__(self, name, distance, damage):
        self.name = name
        self.distance = distance
        self.damage = damage

    def __str__(self):
        return self.name


class Weapons(Enum):

    bow = Weapon("bow", 40, 10)
    short_sword = Weapon("short sword", 1, 7)

    @staticmethod
    def get_by_name(name: str) -> Weapon:
        return Weapons[name].value
