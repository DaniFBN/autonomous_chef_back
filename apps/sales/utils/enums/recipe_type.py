from enum import IntEnum
from apps.utils.default_enum import DefaultEnum


class RecipeType(IntEnum, DefaultEnum):
    Bolo = 0
    Panettone = 1
    EasterEgg = 2
    Pie = 3
    PartySweet = 4
    Default = 5
        