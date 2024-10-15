from __future__ import annotations

from typing import List
from unittest import TestCase

from config import Directions, Tiles
from ed_utils.decorators import number, visibility
from hollows import Hollow
from maze import Maze, MazeCell, Position
from treasure import Treasure


class TestTask3(TestCase):

    @staticmethod
    def reset_visited_maze(maze: Maze) -> None:
        for row in maze.grid:
            for cell in row:
                cell.visited = False

    @staticmethod
    def update_hollow(hollow: Hollow, new_treasures: List[Treasure]) -> None:
        hollow.treasures = new_treasures
        hollow.restructure_hollow()

    @staticmethod
    def count_treasure_totals(treasures: List[Treasure]) -> int:
        # Map the treasures to their values then return the sum of all the treasures
        return sum(map(lambda t: t.value, treasures))

    def force_hollows(self, treasures: List[List[Treasure]]) -> None:
        treasure_index: int = 0
        for row in range(len(self.maze.grid)):
            for col in range(len(self.maze.grid[row])):
                maze_cell: MazeCell = self.maze.grid[row][col]
                if isinstance(maze_cell.tile, Hollow):
                    self.update_hollow(maze_cell.tile, treasures[treasure_index])
                    treasure_index += 1

    def validate_path(self, maze: Maze, path: List[Position]) -> bool:
        def valid_step(step: Position) -> bool:
            return maze.is_valid_position(step)
        self.reset_visited_maze(maze)

        # Check final position is an exit
        fp: Position = path[len(path) - 1]  # Final position
        self.assertTrue(fp in maze.end_positions, f"Expected the final position to be an exit got {fp} ({maze.grid[fp.row][fp.col]})")

        # Check initial position is a start
        self.assertEqual(path[0], maze.start_position, f"Expected the initial position to be the start position got {path[0]}, instead of {maze.start_position}")

        # check if all steps are valid
        valid_steps: List[bool] = list(map(valid_step, path))
        self.assertTrue(all(valid_steps), f"Invalid steps found in the path {path}")

        for step_num, step in enumerate(path):
            # check if the step is a valid move
            if step_num == len(path) - 1:
                continue
            next_step: Position = path[step_num + 1]

            # Check if we can move to the next step
            for direction in Directions:
                next_position: Position = Position(
                    step.row + Maze.directions[direction][0], step.col + Maze.directions[direction][1])
                if next_position == next_step:
                    break
            else:
                self.fail(f"Invalid move from {step} to {next_step}")

    @number("3.0")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_exit_aux_maze_methods(self) -> None:
        # Testing get_available_positions and is_valid_position
        maze: Maze = Maze.load_maze_from_file("task3/maze1.txt")
        for i in range(len(maze.grid)):
            self.assertFalse(maze.is_valid_position(Position(0, i)), "Expected position to be invalid")
        # Test exit tile
        self.assertTrue(maze.is_valid_position(Position(1, 7)), "Expected exit position to be valid")
        self.assertFalse(maze.is_valid_position(Position(1, 8)), "Expected wall position to be invalid")

        # Test player position
        self.assertTrue(maze.is_valid_position(Position(4, 1)), "Expected player position to be valid")
        # Test hollow position
        self.assertTrue(maze.is_valid_position(Position(2, 2)), "Expected Mystic hollow position to be valid")
        self.assertTrue(maze.is_valid_position(Position(2, 7)), "Expected Spooky hollow position to be valid")

        positions: List[Position] = maze.get_available_positions(Position(4, 1))
        self.assertEqual(len(positions), 2, "Expected 2 available positions")
        self.assertTrue(Position(3, 1) in positions, f"Expected position (3, 1) to be available")
        self.assertTrue(Position(4, 2) in positions, "Expected position (4, 2) to be available")

        # All positions should be available
        positions = maze.get_available_positions(Position(3, 4))
        self.assertEqual(len(positions), 4, "Expected 4 available positions")
        expected: List[tuple[int, int]] = [(2, 4), (4, 4), (3, 3), (3, 5)]
        expected: List[Position] = list(map(lambda p: Position(p[0], p[1]), expected))
        for pos in expected:
            self.assertTrue(pos in positions, f"Expected position {pos} to be available")
        # While these two treasures are not the same object they should be considered equal
        """
        Required eq method in treasure.py
        def __eq__(self, value: object) -> bool:
            return isinstance(value, Treasure) and value.value == self.value and value.weight == self.weight
        """
        self.assertEqual(Treasure(1008, 1008), Treasure(1008, 1008), "Treasure equality failed you need to use the __eq__ method provided in the scaffold.")

    @number("3.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_exit_finding_basic(self) -> None:
        maze: Maze = Maze.load_maze_from_file("/sample2.txt")
        student_result: List[Position] | None = maze.find_way_out()
        self.validate_path(maze, student_result)

    @number("3.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_exit_finding_basic_no_exit(self) -> None:
        maze: Maze = Maze.load_maze_from_file("/task3/no_valid_exit.txt")
        self.assertIsNone(maze.find_way_out())

    @number("3.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_exit_finding_traverse_maze_all(self) -> None:
        maze: Maze = Maze.load_maze_from_file("/task3/visit_all.txt")
        self.assertIsNone(maze.find_way_out())
        for row in maze.grid:
            for cell in row:
                if cell.tile != " ":
                    continue
                self.assertTrue(cell.visited, f"Expected all cells to be visited, found {cell} unvisited (position: {cell.position})")

    @number("3.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_take_treasures_no_treasures(self) -> None:
        self.maze: Maze = Maze.load_maze_from_file("/task3/treasures/maze1.txt")
        path: List[tuple[int, int]] = [(3, 1), (2, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (2, 3), (1, 3), (1, 4), (2, 4),
                                       (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (2, 6), (3, 6), (3, 7), (2, 7), (1, 7)]
        path: List[Position] = list(map(lambda p: self.maze.grid[p[0]][p[1]], path))
        # Treasure is value, weight
        mystic_1: List[Treasure] = [Treasure(43, 76)]
        spooky_1: List[Treasure] = [Treasure(45, 4)]
        spooky_2: List[Treasure] = [Treasure(73, 70)]
        treasures: List[List[Treasure]] = [mystic_1, spooky_1, spooky_2]
        self.force_hollows(treasures)
        student_result: List[Treasure] | None = self.maze.take_treasures(path, 3)
        self.assertEqual(student_result, None, f"Expected no treasures to be taken instead got {student_result}")
        # Route with no hollows
        path: List[tuple[int, int]] = [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (2, 8), (1, 8)]
        path: List[MazeCell] = list(map(lambda p: self.maze.grid[p[0]][p[1]], path))

        # Testing a variety of staminas in case you've done something silly
        for sta in [0, 50, 100]:
            treasures: List[Treasure] | None = self.maze.take_treasures(path, sta)
            self.assertEqual(student_result, treasures, f"Expected no treasures to be taken instead got {student_result}")

    @number("3.5")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_take_treasures_basic(self) -> None:
        self.maze: Maze = Maze.load_maze_from_file("/task3/treasures/maze1.txt")
        path: List[tuple[int, int]] = [(3, 1), (2, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (2, 3), (1, 3), (1, 4), (2, 4),
                                       (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (2, 6), (3, 6), (3, 7), (2, 7), (1, 7)]
        path: List[MazeCell] = list(map(lambda p: self.maze.grid[p[0]][p[1]], path))

        # Treasure is value, weight
        mystic_1: List[Treasure] = [Treasure(43, 76)]
        spooky_1: List[Treasure] = [Treasure(45, 4)]
        spooky_2: List[Treasure] = [Treasure(73, 70)]
        treasures: List[List[Treasure]] = [mystic_1, spooky_1, spooky_2]
        self.force_hollows(treasures)
        student_result: List[Treasure] | None = self.maze.take_treasures(path, 3)
        self.assertEqual(student_result, None, f"Expected no treasures to be taken instead got {student_result}")
        # constrained by stamina
        student_result: List[Treasure] | None = self.maze.take_treasures(path, 50)
        self.assertEqual(student_result, [Treasure(45, 4)], f"To take just one treasure from the first spooky hollow instead got: {student_result}")
        # Refill the hollows
        self.force_hollows(treasures)
        student_result: List[Treasure] | None = self.maze.take_treasures(path, 4 + 76 + 70)
        self.assertEqual(student_result, [Treasure(45, 4), Treasure(43, 76), Treasure(73, 70)], f"Expected all treasures to be taken instead got {student_result}")

        # Refill the hollows
        self.force_hollows(treasures)
        student_result: List[Treasure] | None = self.maze.take_treasures(path,  4 + 76 + 70 - 1)
        self.assertEqual(student_result, [Treasure(45, 4), Treasure(43, 76)], f"We expected to take the first two treasures instead got {student_result}")

    @number("3.6")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_take_treasures_multi_ratios(self) -> None:
        self.maze: Maze = Maze.load_maze_from_file("/task3/treasures/maze1.txt")
        path: List[tuple[int, int]] = [(3, 1), (2, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (2, 3), (1, 3), (1, 4), (2, 4),
                                       (3, 4), (3, 5), (2, 5), (1, 5), (1, 6), (2, 6), (3, 6), (3, 7), (2, 7), (1, 7)]
        path: List[MazeCell] = list(map(lambda p: self.maze.grid[p[0]][p[1]], path))
        # Treasure is value, weight
        mystic_1: List[Treasure] = [Treasure(41, 42), Treasure(66, 1), Treasure(7, 73), Treasure(56, 51)]
        spooky_1: List[Treasure] = [Treasure(44, 95), Treasure(60, 38), Treasure(67, 2), Treasure(68, 49)]
        spooky_2: List[Treasure] = [Treasure(81, 93), Treasure(78, 19), Treasure(34, 3), Treasure(15, 65)]
        treasures: List[List[Treasure]] = [mystic_1, spooky_1, spooky_2]
        self.force_hollows(treasures)
        student_result: List[Treasure] | None = self.maze.take_treasures(path, 7)
        expected: List[Treasure] = [Treasure(67, 2), Treasure(66, 1), Treasure(34, 3)]
        self.assertEqual(student_result, expected, f"Incorrect treasures taken {student_result}, expected {expected}")
        student_result: List[Treasure] | None = self.maze.take_treasures(path, 50)
        expected: List[Treasure] = [Treasure(60, 38)]
        self.assertEqual(student_result, expected, f"Incorrect treasures taken {student_result}, expected {expected}")

    @number("3.7")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_take_treasures_not_all_on_path(self) -> None:
        self.maze: Maze = Maze.load_maze_from_file("/task3/treasures/maze1.txt")
        # Path that only has just the one mystic hollow
        path: List[tuple[int, int]] = [(3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3),
                                       (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (2, 8), (1, 8)]
        path: List[MazeCell] = list(map(lambda p: self.maze.grid[p[0]][p[1]], path))
        # Treasure is value, weight
        mystic_1: List[Treasure] = [Treasure(41, 42), Treasure(66, 1), Treasure(7, 73), Treasure(56, 51)]
        spooky_1: List[Treasure] = [Treasure(44, 95), Treasure(60, 38), Treasure(67, 2), Treasure(68, 49)]
        spooky_2: List[Treasure] = [Treasure(81, 93), Treasure(78, 19), Treasure(34, 3), Treasure(15, 65)]
        treasures: List[List[Treasure]] = [mystic_1, spooky_1, spooky_2]
        self.force_hollows(treasures)
        student_result: List[Treasure] | None = self.maze.take_treasures(path, 7)
        expected: List[Treasure] = [Treasure(67, 2)]
        self.assertEqual(student_result, expected, f"Incorrect treasures taken {student_result}, expected {expected}")
        student_result: List[Treasure] | None = self.maze.take_treasures(path, 50)
        expected: List[Treasure] = [Treasure(60, 38)]
        self.assertEqual(student_result, expected, f"Incorrect treasures taken {student_result}, expected {expected}")

    @number("3.7")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_take_treasures_multi_mystics(self) -> None:
        self.maze: Maze = Maze.load_maze_from_file("/task3/treasures/maze2.txt")
        # Path that has 6 mystic hollows
        path: List[tuple[int, int]] = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]
        path: List[MazeCell] = list(map(lambda p: self.maze.grid[p[0]][p[1]], path))

        mystic_1: List[Treasure] = [Treasure(90, 28), Treasure(32, 11), Treasure(94, 34), Treasure(11, 17), Treasure(96, 13), Treasure(55, 71), Treasure(45, 70), Treasure(47, 74), Treasure(35, 99), Treasure(
            38, 83), Treasure(87, 23), Treasure(18, 26), Treasure(50, 16), Treasure(84, 14), Treasure(58, 64), Treasure(97, 30), Treasure(61, 47), Treasure(70, 19), Treasure(51, 6), Treasure(31, 78)]

        # We only have to update the one hollow as they're all the same
        mystic_hollow: Tiles = self.maze.grid[1][2].tile
        self.update_hollow(mystic_hollow, mystic_1)

        student_result: List[Treasure] | None = self.maze.take_treasures(path, 7)
        expected: List[Treasure] = [Treasure(51, 6)]
        self.assertEqual(student_result, expected, f"Incorrect treasures taken {student_result}, expected {expected}")

        # Refill the hollows
        self.update_hollow(mystic_hollow, mystic_1)

        student_result: List[Treasure] | None = self.maze.take_treasures(path, 31)
        expected: List[Treasure] = [Treasure(51, 6), Treasure(96, 13), Treasure(32, 11)]
        self.assertEqual(student_result, expected, f"Incorrect treasures taken {student_result}, expected {expected}")

        # Refill the hollows
        self.update_hollow(mystic_hollow, mystic_1)

        student_result: List[Treasure] | None = self.maze.take_treasures(path, 1008)
        expected: List[Treasure] = [Treasure(51, 6), Treasure(96, 13), Treasure(84, 14), Treasure(87, 23), Treasure(70, 19), Treasure(97, 30)]
        self.assertEqual(student_result, expected, f"Incorrect treasures taken {student_result}, expected {expected}")
