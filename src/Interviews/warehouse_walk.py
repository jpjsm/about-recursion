"""
Find all possible paths to reach a target location, in a warehouse (as an
array of arrays [[...], [...]]), if you can only make RIGHT or DOWN movements.
Values in the 'warehouse' represent 'empty' = '1', 'occupied' = 0; Think of
'can-move-in' <- 'empty', 'cannot-move-in' <- 'occupied'.
"""

from __future__ import annotations  # Needed if using Python < 3.11

from enum import Enum
from typing import List, Set, Tuple


class MOVEMENT(Enum):
    Right = 1
    Down = 2

    @staticmethod
    def NextMove(move: MOVEMENT, row: int, col: int) -> Tuple[int, int]:
        if move == MOVEMENT.Right:
            return (row, col + 1)
        elif move == MOVEMENT.Down:
            return (row + 1, col)
        else:
            raise ValueError(f"Undefined move: {move}")


class Coordinates:
    def __init__(self, row: int, col: int):
        self.Row: int = row
        self.Col: int = col

    def __eq__(self, other) -> bool:
        if not isinstance(other, Coordinates):
            return False
        return self.Row == other.Row and self.Col == other.Col

    def __hash__(self):
        return hash((self.Row, self.Col))

    def __str__(self) -> str:
        return f"[{self.Row}, {self.Col}]"


RIGHT = MOVEMENT.Right
DOWN = MOVEMENT.Down


def can_move(
    pos: Coordinates,
    movement: MOVEMENT,
    warehouse: List[List[int]],
    visited: Set[Coordinates],
) -> bool:
    """Verifies if movement is possible in the direction indicated and has not been visited before

    Args:
        pos (Tuple[int,int]): The position from where the movement starts -> [row, col]
        movement (str): The direction of the movement
        warehouse (List[List[int]]): The location map:
                                    - '1' indicates an empty location
                                    - '0' indicates the location is used

    Returns:
        bool: True: A movement in that location is possible; otherwise False
    """
    if movement not in MOVEMENT:
        return False

    row = pos.Row
    col = pos.Col
    if movement == RIGHT:
        if (
            ((col + 1) >= len(warehouse[row]))
            or warehouse[row][col + 1] == 0
            or Coordinates(row, col + 1) in visited
        ):
            return False
    elif movement == DOWN:
        if (
            ((row + 1) >= len(warehouse))
            or warehouse[row + 1][col] == 0
            or Coordinates(row + 1, col) in visited
        ):
            return False

    return True


def traverse(
    pos: Coordinates,
    target: Coordinates,
    warehouse: List[List[int]],
    walked: List[Coordinates],
    completed: List[List[Coordinates]],
):
    new_walked = [w for w in walked] + [pos]
    if pos == target:
        completed.append(new_walked)
        return

    for move in MOVEMENT:
        visited = set(new_walked)
        if can_move(pos, move, warehouse, visited):
            new_pos = Coordinates(*move.NextMove(move, pos.Row, pos.Col))
            traverse(new_pos, target, warehouse, new_walked, completed)


if __name__ == "__main__":
    warehouse: List[List[int]] = [[1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 1]]
    initial_pos: Coordinates = Coordinates(0, 0)
    target_pos: Coordinates = Coordinates(
        len(warehouse) - 1, len(warehouse[len(warehouse) - 1]) - 1
    )
    walked: List[Coordinates] = []
    completed: List[List[Coordinates]] = []
    traverse(initial_pos, target_pos, warehouse, walked, completed)
    print(f"The possible ways to reach from {initial_pos} to {target_pos} are:")
    for walk in completed:
        print(f"-   {" -> ".join(str(w) for w in walk)}")

    print(f"Total different paths: {len(completed)}")
