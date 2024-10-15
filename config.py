from enum import Enum, IntEnum
"""
THIS FILE CANNOT BE CHANGED IT WILL BE REPLACED ON EDSTEM
AUTOMATICALLY. ANY CHANGES WILL BE OVERWRITTEN
"""

class Tiles(Enum):
    WALL = "#"
    EMPTY = "."  # This is also represented as a " "
    START_POSITION = "P"
    MYSTICAL_HOLLOW = "M"
    SPOOKY_HOLLOW = "S"
    EXIT = "E"


class TreasureConfig(IntEnum):
    MAX_NUMBER_OF_TREASURES = 20
    MIN_NUMBER_OF_TREASURES = 10
    MAX_TREASURE_VALUE = 100
    MAX_TREASURE_WEIGHT = 100


class Directions(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
