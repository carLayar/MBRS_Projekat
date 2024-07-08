from enum import Enum


class FetchType(Enum):
    LAZY = 1
    EAGER = 2
    JOIN = 3
    DEFAULT = 4
    SELECT = 5


