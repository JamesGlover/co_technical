"""Classes dealing with direction."""

from doctest import debug
from enum import Enum
from typing import NamedTuple


class DirectionTuple(NamedTuple):
    """
    Indicates a vector for robot movement.

    Do not use directly, instead access via the Direction Enum.

    """

    x: int
    y: int

class Rotation(Enum):
    LEFT = -1
    RIGHT = 1


class Direction(DirectionTuple, Enum):
    """
    A tuple indicating the direction in which a robot is facing.

    Use the four cardinal directions NORTH, SOUTH, EAST, WEST
    """

    # Pylance mistakenly reports
    # Argument missing for parameter "y"
    NORTH = DirectionTuple(0, 1)  # type: ignore
    EAST = DirectionTuple(1, 0)  # type: ignore
    SOUTH = DirectionTuple(0, -1)  # type: ignore
    WEST = DirectionTuple(-1, 0)  # type: ignore

    def rotate(self, dir: int) -> "Direction":
        """Provide the next direction in the rotation."""
        directions_list = list(Direction)
        new_index = directions_list.index(self) + dir
        return directions_list[new_index]
