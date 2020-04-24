import random
from enum import Enum
from typing import Type


def enum_to_choices(enum: Type[Enum]):
    """Convert enum to django choices."""

    return [(item, item.value) for item in enum]


def enum_to_key_list(enum: Type[Enum]):
    """Convert enum to list of keys."""

    return [item for item in enum]


def random_enum_key(enum: Type[Enum]):
    """Return random enum key."""

    return random.choice(enum_to_key_list(enum))
