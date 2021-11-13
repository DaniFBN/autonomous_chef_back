from enum import Enum


class DefaultEnum(Enum):

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def valid_values(cls):
        length = len(cls.choices())

        values = []
        for i in range(0, length):
            values.append(i)

        return values
