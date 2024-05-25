from co_technical import Table, Position
from pytest import mark as m


@m.describe("Table")
class TestTable:
    @m.it("can be created with dimensions")
    def test_can_be_created_with_dimensions(self) -> None:
        assert type(Table(3, 4)) is Table

    @m.describe("within_table_bounds")
    @m.context("with values in range")
    @m.it("returns true")
    def test_within_table_bounds_in_range(self) -> None:
        table = Table(5,5)
        position = Position(3,3)
        assert table.within_table_bounds(position)

    @m.describe("within_table_bounds")
    @m.context("with values of 0")
    @m.it("returns true")
    def test_within_table_bounds_zero_in_range(self) -> None:
        table = Table(5,5)
        position = Position(0,0)
        assert table.within_table_bounds(position)

    @m.describe("within_table_bounds")
    @m.context("with values on edge of range")
    @m.it("returns true")
    def test_within_table_bounds_edge_of_range(self) -> None:
        table = Table(5,5)
        position = Position(5,5)
        assert table.within_table_bounds(position)


    @m.describe("within_table_bounds")
    @m.context("with values out of range")
    @m.it("returns false")
    def test_within_table_bounds_out_of_range(self) -> None:
        table = Table(5,5)
        position = Position(3,6)
        assert not table.within_table_bounds(position)

    @m.describe("within_table_bounds")
    @m.context("with negative values out of range")
    @m.it("returns false")
    def test_within_table_bounds_negative_out_of_range(self) -> None:
        table = Table(5,5)
        position = Position(-1,-1)
        assert not table.within_table_bounds(position)