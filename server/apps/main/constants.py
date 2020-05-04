from enum import Enum


class SubjectTypeEnum(Enum):
    HUMAN = "human"
    ELF = "elf"
    HALF_ELF = "half_elf"
    GNOME = "gnome"
    DWARF = "dwarf"
    GOBLIN = "goblin"


class ColorEnum(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
