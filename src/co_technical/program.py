from collections.abc import Generator
from fileinput import FileInput
from typing import IO

from co_technical.direction import Direction
from co_technical.position import Position
from co_technical.robot import Robot
from co_technical.table import Table


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
        for instruction in self._instructions():
            self._parse(instruction)

    def _parse(self, instruction: str) -> bool:
        match instruction.split():
            case ["PLACE", args]:
                return self._place(args)
            case ["MOVE"]:
                return self._robot.move()
            case ["LEFT"]:
                return self._robot.left()
            case ["RIGHT"]:
                return self._robot.right()
            case ["REPORT"]:
                return self._report()
            case _:
                return False

    def _place(self, args: str) -> bool:
        match args.split(","):
            case [x, y, direction_name]:
                try:
                    position = Position(int(x), int(y))
                    direction = Direction[direction_name]
                    return self._robot.place(position, direction, self._table)
                except (KeyError, ValueError):
                    return False
            case _:
                return False

    def _report(self) -> bool:
        report = self._robot.report()
        if report:
            print(report)
        return report is not None

    def _instructions(self) -> Generator[str, None, None]:
        for instruction_line in self._command_input:
            instruction = instruction_line.strip()
            if instruction:
                yield instruction
