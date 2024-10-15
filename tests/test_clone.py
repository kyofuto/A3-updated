from __future__ import annotations
import os
from unittest import TestCase

from ed_utils.decorators import number, visibility


"""
As this assignment relies on file io it's important that we have the correct files in the correct directories.
And that you have the correct working directory when running the tests.

This test will help you test and diagnose this issue.

There are no marks awarded for this test, it's just to help you get started.
"""


class TestSetup(TestCase):
    @number("0.0")
    @visibility(visibility.VISIBILITY_HIDDEN)
    def test_maze_files(self) -> None:
        """
        Checking if /mazes directory exists
        if this test fails, it likely means you have not cloned the repository correctly
        or
        you perhaps are running the tests from the wrong directory.
        You should have the following directory structure:
        .
        ├── JetBrains.gitignore
        ├── algorithms
        │   ├── __init__.py
        │   ├── binary_search.py
        │   ├── mergesort.py
        │   └── quicksort.py
        ├── betterbst.py
        ├── config.py
        ├── data_structures
        │   ├── __init__.py
        │   ├── abstract_list.py
        │   ├── aset.py
        │   ├── bset.py
        │   ├── bst.py
        │   ├── hash_table.py
        │   ├── heap.py
        │   ├── linked_list.py
        │   ├── linked_queue.py
        │   ├── linked_stack.py
        │   ├── node.py
        │   ├── printer.py
        │   ├── queue_adt.py
        │   ├── referential_array.py
        │   ├── set.py
        │   └── stack_adt.py
        ├── ed_utils
        │   ├── __init__.py
        │   └── decorators.py
        ├── hollows.py
        ├── maze.py
        ├── mazes
        │   ├── positions_sample.txt
        │   ├── sample.txt
        │   ├── sample2.txt
        │   └── task3
        │       ├── maze1.txt
        │       ├── maze2.txt
        │       ├── maze3.txt
        │       ├── maze4.txt
        │       ├── no_valid_exit.txt
        │       ├── treasures
        │       │   └── test1.txt
        │       └── visit_all.txt
        ├── random_gen.py
        ├── readme.md
        ├── run_tests.py
        ├── tests
        │   ├── __init__.py
        │   ├── test_clone.py
        │   ├── test_task1.py
        │   ├── test_task2.py
        │   └── test_task3.py
        └── treasure.py

        """
        self.assertTrue(os.path.exists("mazes"), "/mazes directory does not exist")
        self.assertTrue(os.path.exists("mazes/sample.txt"), "/mazes/sample.txt does not exist please see the testcase for more information.")
        self.assertTrue(os.path.exists("mazes/sample2.txt"), "/mazes/sample2.txt does not exist please see the testcase for more information.")
