from __future__ import annotations

from config import TreasureConfig
from random_gen import RandomGen
from typing import List


class Treasure:
    def __init__(self, value: int, weight: int) -> None:
        """
        Complexity:
            O(1)

        Args:
            value (int): The value of this treasure
            weight (int): The weight of this treasure
        """
        self.value: int = value
        self.weight: int = weight

    def __eq__(self, value: object) -> bool:
        # Do not monitfy this function
        return isinstance(value, Treasure) and value.value == self.value and value.weight == self.weight

    def __str__(self) -> str:
        return f"Treasure: {self.value} ({self.weight}kg)"

    def __repr__(self) -> str:
        return str(self)


def generate_treasures() -> List[Treasure]:
    """
    This function will generate a random list of treasures with random values and weights.
    The weights, values and ratios of the treasures will be unique within the output list.

    Returns:
        list(Treasure): A random list of treasures

    Complexity:
        Best Case Complexity: O(N)
        Worst Case Complexity: O(N) where N is TreasureConfig.MAX_NUMBER_OF_TREASURES.value

        This assumes the randint and python set operations can be done in O(1) time.
    """
    number_of_treasures = RandomGen.randint(TreasureConfig.MIN_NUMBER_OF_TREASURES.value,
                                            TreasureConfig.MAX_NUMBER_OF_TREASURES.value)

    hollow_treasures: List[Treasure | None] = [None] * number_of_treasures
    ratios: set[float] = set()
    weights_used: set[int] = set()
    values_used: set[int] = set()

    treasure_count: int = 0
    while treasure_count < number_of_treasures:
        weight: int = RandomGen.randint(1, TreasureConfig.MAX_TREASURE_WEIGHT.value)
        value: int = RandomGen.randint(1, TreasureConfig.MAX_TREASURE_WEIGHT.value)
        ratio: float = value / weight

        if ratio not in ratios and weight not in weights_used and value not in values_used:
            hollow_treasures[treasure_count] = Treasure(value, weight)
            ratios.add(ratio)
            weights_used.add(weight)
            values_used.add(value)
            treasure_count += 1

    return hollow_treasures
