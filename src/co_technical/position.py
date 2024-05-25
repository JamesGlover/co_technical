"""Includes position class to handle robot position."""

from typing import NamedTuple


class Position(NamedTuple):
    """
    Simple tuple representing X,Y coordinates.

    Params:
    x (int): The X (East-West) Co-ordinate
    y (int): The Y (North-South) Co-ordinate
    """

    x: int
    y: int
