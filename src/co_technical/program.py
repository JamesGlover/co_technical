from fileinput import FileInput
from typing import IO

from co_technical.direction import Direction
from co_technical.position import Position
from co_technical.robot import Robot
from co_technical.table import Table

PLACE_ARGUMENTS = 3


class Program:
    """Handle loading of instructions from stdin or a file and passing them to robot."""

    _command_input: IO[str] | FileInput[str]
    _robot: Robot
    _table: Table

    def __init__(self, command_input: IO[str] | FileInput[str]) -> None:
        """Create a new program for handling commands."""
        self._command_input = command_input
        self._robot = Robot()
        # We'll hardcode the table dimensions here for now.
        self._table = Table(5, 5)

    def execute(self) -> None:
        """Load and execute the commands in command_input."""
        for instruction in self._command_input:
            self._parse(instruction)

    def _parse(self, instruction: str) -> bool:
        command, *args = instruction.split()
        match command:
            case "PLACE":
                return self._place(*args)
            case "MOVE":
                return self._robot.move()
            case "LEFT":
                return self._robot.left()
            case "RIGHT":
                return self._robot.right()
            case "REPORT":
                return self._report()
            case _:
                # Unknown command. Undefined behaviour via spec.
                # Ignoring
                return False

    def _place(self, args: str) -> bool:
        provided_args: list[str] = args.split(",")
        if len(provided_args) != PLACE_ARGUMENTS:
            return False

        x, y, direct_s = provided_args
        position = Position(int(x), int(y))
        direction = Direction[direct_s]
        return self._robot.place(position, direction, self._table)

    def _report(self) -> bool:
        report = self._robot.report()
        if report:
            print(report)
        return report is not None
