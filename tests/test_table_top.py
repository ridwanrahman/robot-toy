import pytest

from toy_robot.table_top import TableTop


class TestTableTop:

    def test_tabletop(self):
        test_length = 5
        test_width = 5
        test_table_top = TableTop(
            length=test_length,
            width=test_width
        )
        assert(test_table_top.get_length() == test_length)
        assert(test_table_top.get_width() == test_width)

    @pytest.mark.parametrize("test_input, expected", [
        ((2, 3), True),
        ((5, 5), True),
        ((6, 6), False),
        ((0, 0), True)
    ])
    def test_validate_with_dimensions(self, test_input, expected):
        """
        Test to check if test_inputs are within the dimensions of the tabletop (5x5)

        Parameters
        ----------
        test_input: x: int, y:int
             The x, y coordinates to check if it is within the dimensions of the tabletop
        :param expected: bool
            True if within tabletop, False if not
        """
        test_length = 5
        test_width = 5
        test_table_top = TableTop(
            length=test_length,
            width=test_width
        )
        response = test_table_top.validate_with_dimensions(test_input[0], test_input[1])
        assert (response == expected)
