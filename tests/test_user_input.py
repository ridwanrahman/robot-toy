import pytest
import logging

from toy_robot.user_input import UserInput


class TestPlaceCommand:
    """
    Test the UserInput class
    """

    @pytest.mark.parametrize("test_input, expected", [
        ('PLACE 0, 0, NORTH\n', ['PLACE', 0, 0, 'NORTH']),
        ('PLACE 1, 2, WEST\n', ['PLACE', 1, 2, 'WEST']),
        ('PLACE 3, 4, SOUTH\n', ['PLACE', 3, 4, 'SOUTH'])
    ])
    def test_correct_place_command(self, test_input, expected):
        """
        Functions in UserInput() class take care of each type of input
        The hanndle function takes care of 'PLACE' command
        """
        list_line = test_input.rstrip('\n').split(" ")
        user_input = UserInput()
        result = user_input.handle_place(list_line)
        assert result == expected

    @pytest.mark.parametrize("test_input", [
        'PLACE 0, 0, NORTHEAST\n',
        'PLACE 0, 0, SOUTHEAST\n',
        'PLACE 0, 0, abcdef\n',
        'PLACE , 0, NORTH\n',
        'PLACE 0, , EAST\n'
    ])
    def test_incorrect_place_direction_command(self, caplog, test_input):
        caplog.set_level(logging.DEBUG)
        user_input = UserInput()
        user_input.process_file_line(test_input)
        assert (
            "ERROR: Please ensure format is PLACE X, Y, F, as program starts after PLACE command"
            in str(caplog.records)
        )

    @pytest.mark.parametrize("test_input, expected", [
        ('MOVE 0, 0, NORTHEAST\n', 'ERROR: Incorrect MOVE command provided in input file'),
        ('REPORT 0, 0, NORTHEAST\n', 'ERROR: Incorrect REPORT command provided in input file'),
        ('LEFT 0, 0, NORTHEAST\n', 'ERROR: Incorrect LEFT/RIGHT command provided in input file'),
        ('RIGHT 0, 0, NORTHEAST\n', 'ERROR: Incorrect LEFT/RIGHT command provided in input file'),
    ])
    def test_incorrect_place_command(self, caplog, test_input, expected):
        """
        Testing incorrect data
        """
        caplog.set_level(logging.DEBUG)
        user_input = UserInput()
        user_input.process_file_line(test_input)
        assert (
                expected
                in str(caplog.records)
        )

    @pytest.mark.parametrize("test_input, expected", [
        ('abcdef', 'ERROR: Incorrect command: abcdef'),
    ])
    def test_incorrect_command(self, caplog, test_input, expected):
        """
        Testing incorrect commands
        """
        caplog.set_level(logging.DEBUG)
        user_input = UserInput()
        user_input.process_file_line(test_input)
        assert (
            expected
            in str(caplog.records)
        )


class TestMoveCommand:

    @pytest.mark.parametrize("test_input", [
        ['MOVE'],
    ])
    def test_correct_move_command(self, test_input):
        user_input = UserInput()
        result = user_input.handle_move(test_input)
        assert(result == 'MOVE')


class TestReportCommand:
    @pytest.mark.parametrize("test_input", [
        ['REPORT'],
    ])
    def test_correct_report_command(self, test_input):
        user_input = UserInput()
        result = user_input.handle_report(test_input)
        assert (result == 'REPORT')


class TestDirectionCommand:
    @pytest.mark.parametrize("test_input, expected", [
        (['LEFT'], 'LEFT'),
        (['RIGHT'], 'RIGHT'),
    ])
    def test_correct_direction_command(self, test_input, expected):
        user_input = UserInput()
        result = user_input.handle_direction(test_input)
        assert (result == expected)
