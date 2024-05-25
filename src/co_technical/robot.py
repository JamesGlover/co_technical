from co_technical.direction import Direction
from co_technical.position import Position
from co_technical.table import Table


class Robot:
    """
    A simulated robot able to move around an environment.

    A robot keeps track of its position and direction.
    It can be moved round the environment, placed in a new position
    or report its position and direction.

    A robot will not have a position or direction until placed.

    A robot will ignore any commands that cause it to move outside its
    environment,
    """

    _position: Position | None
    _direction: Direction | None
    _environment: Table | None

    def __init__(self) -> None:
        """Create a new robot with no position or direction."""
        self._position = None
        self._direction = None

    @property
    def x(self) -> int | None:
        """X coordinate (East-West) of robot."""
        if self._position:
            return self._position.x

    @property
    def y(self) -> int | None:
        """Y coordinate (North-South) of robot."""
        if self._position:
            return self._position.y

    @property
    def direction(self) -> str | None:
        """Name of direction of robot."""
        if self._direction:
            return self._direction.name

    def report(self) -> None | str:
        """
        Return the robot position if placed None otherwise.

        Position is reported in the format:
        x,y,dir

        eg. 0,0,EAST
        """
        if self._position and self._direction:
            return f"{self.x},{self.y},{self.direction}"

    def place(
        self, position: Position, direction: Direction, environment: Table
    ) -> bool:
        """
        Place the robot at position facing direction in the environment.

        Checks the validity of the position, if the position is invalid the
        robot will not be placed, and the function returns False.

        Currently environment will be a Table.

        Args:
        position (Position): The position to place the robot
        direction (Direction): The direction in which it should face
        environment (Table): The environment in which to place the robot.

        """
        if environment.within_bounds(position):
            self._position = position
            self._direction = direction
            self._environment = environment
            return True
        else:
            return False

    def move(self) -> bool:
        """
        Move the robot in direction if placed.

        Checks the validity of the updated position according to the environment.
        If the move will be invalid and move the robot out of bounds then it will
        not move, and the function returns False.

        """
        if self._position and self._direction and self._environment:
            new_position: Position = self._position.move(self._direction)

            if self._environment.within_bounds(new_position):
                self._position = new_position
                return True

        return False

    def left(self) -> bool:
        """
        Rotate the robot to the left if placed.

        If the robot has not been placed does nothing. Returns False.
        """
        return self._rotate(-1)

    def right(self) -> bool:
        """
        Rotate the robot to the right if placed.

        If the robot has not been placed does nothing. Returns False.
        """
        return self._rotate(1)

    def _rotate(self, direction: int) -> bool:
        if self._direction:
            self._direction = self._direction.rotate(direction)
            return True
        else:
            return False
