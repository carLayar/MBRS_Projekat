from enum import Enum


class IdStrategy(Enum):
    IDENTITY = 1
    SEQUENCE = 2
    TABLE = 3
    AUTO = 4
    