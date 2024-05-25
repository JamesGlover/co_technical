"""Module for the Table class."""

from co_technical import Position


class Table:
    """
    An environment on which a Robot can move.

    Has two dimensions, indicating its size and can report if a position is out of
    bounds.
    """

    _x: int
    _y: int

    def __init__(self, x: int, y: int) -> None:
        """
        Create a new table.

        Args:
          x (int): The x (East-West) dimensions of the table
          y (int): The y (North-South) dimensions of the table

        """
        self._x = x
        self._y = y

    def within_bounds(self, position: Position) -> bool:
        """
        Indicate whether position is within the bounds of the table.

        Args:
        position (Position): The position to test

        Returns:
        bool: True if within bounds, False otherwise.

        """
        return (position.x >= 0 and position.x <= self._x) and (
            position.y >= 0 and position.y <= self._y
        )
