from enum import IntEnum
from apps.utils.default_enum import DefaultEnum


class UnitMeasurement(IntEnum, DefaultEnum):
    Gram = 0
    Milligram = 1
    Kilogram = 2
    Liter = 3
    Millilitem = 4
    Unity = 5
