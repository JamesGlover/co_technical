from co_technical import Program
from pytest import CaptureFixture
from pytest import mark as m


def execute_for(filename: str) -> str:
    with open(f"./examples/{filename}") as content:
        Program(content).execute()


@m.describe("The full application")
class TestCoTechnical:
    """Provides a few tests to test overall behaviour of the application."""

    @m.context("when provided with the input in example a of the specifications")
    @m.it("outputs the expected output of 0,1,NORTH on REPORT")
    def test_provided_example_a(self, capsys: CaptureFixture[str]) -> None:
        execute_for("example_a")
        captured = capsys.readouterr()
        assert captured.out == "0,1,NORTH\n"

    @m.context("when provided with the input in example b of the specifications")
    @m.it("outputs the expected output of 0,0,WEST on REPORT")
    def test_provided_example_b(self, capsys: CaptureFixture[str]) -> None:
        execute_for("example_b")
        captured = capsys.readouterr()
        assert captured.out == "0,0,WEST\n"

    @m.context("when provided with the input in example c of the specifications")
    @m.it("outputs the expected output of 3,3,NORTH on REPORT")
    def test_provided_example_c(self, capsys: CaptureFixture[str]) -> None:
        execute_for("example_c")
        captured = capsys.readouterr()
        assert captured.out == "3,3,NORTH\n"

    @m.context("when provided with the input in which movements occur before placement")
    @m.it("ignores the movements before placement")
    def test_move_before_place(self, capsys: CaptureFixture[str]) -> None:
        execute_for("move_before_place")
        captured = capsys.readouterr()
        assert captured.out == "1,0,EAST\n"

    @m.context("when provided with instructions that move the robot out of bounds")
    @m.it("ignores the movements that would send it out of bounds")
    def test_move_out_of_bounds_ignored(self, capsys: CaptureFixture[str]) -> None:
        execute_for("move_out_of_bounds_ignored")
        captured = capsys.readouterr()
        assert captured.out == "1,0,EAST\n"

    @m.context("when asked to report before it is places")
    @m.it("ignores the REPORT command and outputs nothing")
    def test_report_without_place(self, capsys: CaptureFixture[str]) -> None:
        execute_for("report_without_place")
        captured = capsys.readouterr()
        assert captured.out == ""

    @m.context("when given invalid commands")
    @m.it("ignores the commands and outputs nothing")
    def test_report_with_invalid_commands(self, capsys: CaptureFixture[str]) -> None:
        execute_for("with_invalid_commands")
        captured = capsys.readouterr()
        assert captured.out == ""
