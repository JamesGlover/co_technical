"""Includes position class to handle robot position."""

from typing import NamedTuple

from co_technical.direction import DirectionTuple


class Position(NamedTuple):
    """
    Simple tuple representing X,Y coordinates.

    Params:
    x (int): The X (East-West) Co-ordinate
    y (int): The Y (North-South) Co-ordinate
    """

    x: int
    y: int

    def move(self, vector: DirectionTuple) -> "Position":
        """Return a new position having moved one step in direction."""
        return Position(self.x + vector.x, self.y + vector.y)
