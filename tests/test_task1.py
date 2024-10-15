from __future__ import annotations

from random import Random
from typing import List, Tuple
from unittest import TestCase

from betterbst import BetterBST
from ed_utils.decorators import number, visibility


class TestTask1(TestCase):
    @number("1.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_better_bst_operations(self) -> None:
        numbers: List[tuple[int, str]] = [(x, str(x)) for x in range(1, 17)]
        better_bst: BetterBST = BetterBST(numbers)
        self.assertEqual(len(better_bst), 16, "There should be 15 elements in the bst")

        self.assertEqual(better_bst.get_minimal(better_bst.root).key, 1, f"Expected 1 as the minimal key got {better_bst.get_minimal(better_bst.root)}")
        self.assertEqual(better_bst.get_maximal(better_bst.root).key, 16, f"Expected 16 as the maximal key got {better_bst.get_maximal(better_bst.root)}")

        del better_bst[1]

        self.assertEqual(better_bst.get_minimal(better_bst.root).key, 2, f"Expected 2 as the minimal key got {better_bst.get_minimal(better_bst.root)}")

    @number("1.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_bst_balance(self):
        numbers: List[tuple[int, str]] = [(x, str(x)) for x in range(1, 17)]
        better_bst: BetterBST = BetterBST(numbers)
        self.assertEqual(better_bst.is_balanced(), True, "The tree should be balanced")

        numbers: List[int] = [1964, 586, 888, 416, 3088, 1736, 2690, 2502, 171, 767, 3053, 2156, 536,
                              486, 560, 601, 2140, 822, 1554, 2932, 505, 1245, 1639, 2179, 1045, 1542, 179, 2639, 2961]
        numbers: List[Tuple[int, str]] = [(x, str(x)) for x in numbers]
        better_bst = BetterBST(numbers)
        self.assertEqual(better_bst.is_balanced(), True, "The tree should be balanced")

    @number("1.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_bst_balance_2(self):
        numbers: List[int] = [12482961, 28677579, 21589567, 29180361, 1465047, 20325086, 31013035, 10389326, 22283568, 28114676, 21715872, 36247, 30821720, 23565440, 25479803, 24206692, 19184335, 11410531, 6677957, 17108693, 9152417, 20235004,
                              27498797, 16228428, 13405296, 16604570, 24732332, 26675257, 18101333, 21295517, 15406486, 20504994, 5417150, 2550562, 19789429, 26821312, 14283105, 1523316, 815628, 22664586, 11186756, 2891723, 24207674, 23283113, 13113168]
        numbers: List[Tuple[int, str]] = [(x, str(x)) for x in numbers]
        better_bst = BetterBST(numbers)

        self.assertEqual(better_bst.is_balanced(), True, "The tree should be balanced")
