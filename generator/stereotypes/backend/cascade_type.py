from enum import Enum


class CascadeType(Enum):
    ALL = 1
    PERSIST = 2
    MERGE = 3
    REMOVE = 4
    REFRESH = 5
    DETACH = 6
