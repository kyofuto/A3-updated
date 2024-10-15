from __future__ import annotations

from typing import List
from unittest import TestCase

from ed_utils.decorators import number, visibility
from hollows import Hollow, MysticalHollow, SpookyHollow
from treasure import Treasure


class TestTask2(TestCase):
    @number("2.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_optimality_basic(self) -> None:
        treasures: List[Treasure] = [Treasure(x, 100) for x in range(4)]
        treasures.append(Treasure(100, 100))
        def treasure_gen(x): return treasures
        Hollow.gen_treasures = treasure_gen

        spooky_hollow: SpookyHollow = SpookyHollow()
        self.assertIsNone(spooky_hollow.get_optimal_treasure(2), "Spooky hollow: Expected None as all the treasures are greater than backpack capacity")

        mystical_hollow: MysticalHollow = MysticalHollow()
        current_treasure: Treasure | None = mystical_hollow.get_optimal_treasure(2)
        self.assertIsNone(current_treasure, "Mystical hollow: Expected None as all the treasures are greater than backpack capacity")
        current_treasure = mystical_hollow.get_optimal_treasure(100)
        self.assertIsNotNone(current_treasure, "Mystical hollow: There should be a treasure available for a backpack capacity of 100")
        self.assertEqual(type(current_treasure), Treasure, "Mystical hollow: Expected a treasure object")
        self.assertEqual(current_treasure, treasures[-1], "Mystical hollow: Expected the last treasure as the optimal treasure")
        current_treasure = spooky_hollow.get_optimal_treasure(100)
        self.assertIsNotNone(current_treasure, "Spooky hollow: There should be a treasure available for backpack capacity 100")
        self.assertEqual(current_treasure, treasures[-1], f"Spooky hollow: There was a better treasure available for backpack capacity 100")

    @number("2.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_getting_all_treasures_hollow(self) -> None:
        num_treasures: int = 10
        treasures: List[Treasure] = [Treasure(100, 100 - x) for x in range(1, 10)]
        def treasure_gen(_): return treasures
        Hollow.gen_treasures = treasure_gen

        spooky_hollow: SpookyHollow = SpookyHollow()
        self.assertEqual(len(spooky_hollow), len(treasures), f"Expected {len(treasures)} treasures after restructuring your hollow you have {len(spooky_hollow)} treasures")

        results: List[Treasure] = []
        for n in range(num_treasures-1):
            treasure: Treasure | None = spooky_hollow.get_optimal_treasure(100)
            self.assertIsNotNone(treasure, "Expected a treasure object")
            self.assertEqual(type(treasure), Treasure, "Expected a treasure object")
            results.append(treasure)

        self.assertEqual(len(spooky_hollow), 0, "Expected all treasures to be removed from the hollow")
        for idx, student_result in enumerate(results):
            expected: Treasure = treasures[-(idx+1)]
            self.assertEqual(student_result, expected, f"Issue with treasure #{idx + 1}:\nExpected {expected} but got {student_result}, it seems you have removed the wrong treasure")

    @number("2.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_empty_hollows(self) -> None:
        treasures: List[Treasure] = [Treasure(1, 1)]
        def treasure_gen(x): return treasures
        Hollow.gen_treasures = treasure_gen

        spooky_hollow: SpookyHollow = SpookyHollow()
        mystical_hollow: MysticalHollow = MysticalHollow()
        spooky_hollow.get_optimal_treasure(100)
        for _ in range(10):
            self.assertIsNone(spooky_hollow.get_optimal_treasure(1), "Expected None as all the treasures are removed")
            self.assertIsNone(spooky_hollow.get_optimal_treasure(0), "Expected None as all the treasures are removed")

        mystical_hollow.get_optimal_treasure(100)
        for _ in range(10):
            self.assertIsNone(mystical_hollow.get_optimal_treasure(1), "Expected None as all the treasures are removed")
            self.assertIsNone(mystical_hollow.get_optimal_treasure(0), "Expected None as all the treasures are removed")

    @number("2.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_heavy_hollows(self) -> None:
        treasures: List[Treasure] = [Treasure(1, 2), Treasure(300, 300)]
        def treasure_gen(x): return treasures
        Hollow.gen_treasures = treasure_gen

        spooky_hollow: SpookyHollow = SpookyHollow()
        mystical_hollow: MysticalHollow = MysticalHollow()
        spooky_hollow.get_optimal_treasure(100)
        for _ in range(10):
            self.assertIsNone(spooky_hollow.get_optimal_treasure(0), "Expected None as the only treasures are heavier than provided backpack capacity")
            self.assertIsNone(spooky_hollow.get_optimal_treasure(0), "Expected None as the only treasures are heavier than provided backpack capacity")

        mystical_hollow.get_optimal_treasure(100)
        for _ in range(10):
            self.assertIsNone(mystical_hollow.get_optimal_treasure(1), "Expected None as the only treasures are heavier than provided backpack capacity")
            self.assertIsNone(mystical_hollow.get_optimal_treasure(0), "Expected None as the only treasures are heavier than provided backpack capacity")
