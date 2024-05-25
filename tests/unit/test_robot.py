from co_technical import Direction, Position, Robot, Table
from pytest import fixture
from pytest import mark as m


@fixture
def table() -> Table:
    return Table(5, 5)


@fixture
def robot() -> Robot:
    return Robot()


@m.describe("Robot")
class TestRobot:
    @m.it("can be created with no arguments")
    def test_can_be_created_with_dimensions(self) -> None:
        assert type(Robot()) is Robot

    @m.describe("report")
    @m.context("before placement")
    @m.it("returns None")
    def test_report_before_place(self, robot: Robot) -> None:
        assert robot.report() is None

    @m.describe("report")
    @m.context("after placement")
    @m.it("returns the position")
    def test_report_after_place(self, robot: Robot, table: Table) -> None:
        robot.place(Position(3, 3), Direction.NORTH, table)
        assert robot.report() == "3,3,NORTH"

    @m.describe("place")
    @m.context("outside table bounds")
    @m.it("is ignored")
    def test_place_out_of_bounds(self, table: Table, robot: Robot) -> None:
        result = robot.place(Position(6, 6), Direction.NORTH, table)
        assert not result
        assert robot.report() is None

    @m.describe("place")
    @m.context("inside table bounds")
    @m.it("is placed")
    def test_place_inside_bounds(self, table: Table, robot: Robot) -> None:
        result = robot.place(Position(3, 3), Direction.NORTH, table)
        assert result

    @m.describe("move")
    @m.context("when valid and facing north")
    @m.it("moves in the given direction")
    def test_move_when_valid_facing_north(self, table: Table, robot: Robot) -> None:
        robot.place(Position(0, 0), Direction.NORTH, table)
        assert robot.move()
        assert robot.x == 0
        assert robot.y == 1

    @m.describe("move")
    @m.context("when valid and facing east")
    @m.it("moves in the given direction")
    def test_move_when_valid_facing_east(self, table: Table, robot: Robot) -> None:
        robot.place(Position(0, 0), Direction.EAST, table)
        assert robot.move()
        assert robot.x == 1
        assert robot.y == 0

    @m.describe("move")
    @m.context("when invalid and facing south")
    @m.it("does not move")
    def test_move_when_invalid_facing_south(self, table: Table, robot: Robot) -> None:
        robot.place(Position(0, 0), Direction.SOUTH, table)
        assert not robot.move()
        assert robot.y == 0
        assert robot.y == 0

    @m.describe("left")
    @m.context("when not on the table")
    @m.it("will be ignored")
    def test_left_when_not_on_table_wont_rotate(self, robot: Robot) -> None:
        assert not robot.left()
        assert robot.direction is None

    @m.describe("left")
    @m.context("when facing NORTH")
    @m.it("will face west")
    def test_left_will_rotate_left(self, robot: Robot, table: Table) -> None:
        robot.place(Position(0, 0), Direction.NORTH, table)
        assert robot.left()
        assert robot.direction == "WEST"

    @m.describe("right")
    @m.context("when not on the table")
    @m.it("will be ignored")
    def test_right_when_not_on_table_wont_rotate(self, robot: Robot, table: Table) -> None:
        assert not robot.right()
        assert robot.direction is None

    @m.describe("right")
    @m.context("when facing NORTH")
    @m.it("will face east")
    def test_right_will_rotate_right(self, robot: Robot, table: Table) -> None:
        robot.place(Position(0, 0), Direction.NORTH, table)
        assert robot.right()
        assert robot.direction == "EAST"

    @m.describe("left")
    @m.context("when called four times")
    @m.it("will face where it started")
    def test_right_will_rotate_360(self, robot: Robot, table: Table) -> None:
        robot.place(Position(0, 0), Direction.NORTH, table)
        robot.left()
        robot.left()
        robot.left()
        robot.left()
        assert robot.direction == "NORTH"
