import pytest
import logging

from toy_robot.user_input import UserInput

class TestPlaceCommand():

    @pytest.mark.parametrize("test_input, expected", [
        ('PLACE 0, 0, NORTH\n', ['PLACE', 0, 0, 'NORTH']),
        ('PLACE 1, 2, WEST\n', ['PLACE', 1, 2, 'WEST']),
        ('PLACE 3, 4, SOUTH\n', ['PLACE', 3, 4, 'SOUTH'])
    ])
    def test_correct_place_command(self, test_input, expected):
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
            "Error in place command. Please ensure format is PLACE X, Y, F"
            in str(caplog.records)
        )

    @pytest.mark.parametrize("test_input", [
        'MOVE 0, 0, NORTHEAST\n',
        'REPORT 0, 0, NORTHEAST\n',
        'LEFT 0, 0, NORTHEAST\n',
        'RIGHT 0, 0, NORTHEAST\n',
    ])
    def test_incorrect_place_command(self, caplog, test_input):
        caplog.set_level(logging.DEBUG)
        user_input = UserInput()
        user_input.process_file_line(test_input)
        assert (
                f"Incorrect command"
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
