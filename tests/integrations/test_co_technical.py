from pytest import mark as m


def output_for(filename: str) -> str:
    with open(f"./examples/{filename}") as content:
        return content.read()


@m.describe("The full application")
class TestCoTechnical:
    """Provides a few tests to test overall behaviour of the application."""

    @m.xfail(reason="pending implementation")
    @m.context("when provided with the input in example a of the specifications")
    @m.it("outputs the expected output of 0,1,NORTH on REPORT")
    def test_provided_example_a(self) -> None:
        assert output_for("example_a") == "0,1,NORTH"

    @m.xfail(reason="pending implementation")
    @m.context("when provided with the input in example b of the specifications")
    @m.it("outputs the expected output of 0,0,WEST on REPORT")
    def test_provided_example_b(self) -> None:
        assert output_for("example_b") == "0,0,WEST"

    @m.xfail(reason="pending implementation")
    @m.context("when provided with the input in example c of the specifications")
    @m.it("outputs the expected output of 3,3,NORTH on REPORT")
    def test_provided_example_c(self) -> None:
        assert output_for("example_c") == "3,3,NORTH"

    @m.xfail(reason="pending implementation")
    @m.context("when provided with the input in which movements occur before placement")
    @m.it("ignores the movements before placement")
    def test_move_before_place(self) -> None:
        assert output_for("move_before_place") == "1,0,EAST"

    @m.xfail(reason="pending implementation")
    @m.context("when provided with instructions that move the robot out of bounds")
    @m.it("ignores the movements that would send it out of bounds")
    def test_move_out_of_bounds_ignored(self) -> None:
        assert output_for("move_out_of_bounds_ignored") == "1,0,EAST"

    @m.xfail(reason="pending implementation")
    @m.context("when asked to report before it is places")
    @m.it("ignores the REPORT command and outputs nothing")
    def test_report_without_place(self) -> None:
        assert output_for("report") is None
