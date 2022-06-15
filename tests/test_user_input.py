import pytest
import logging

from toy_robot.errors import PlaceCommandError, EmptyCommandError
from toy_robot.user_input import UserInput

class TestUserInput:

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
        ('PLACE 0, 0, NORTHEAST\n'),
        ('PLACE 0, 0, SOUTHEAST\n'),
        ('PLACE 0, 0, abcdef\n')
    ])
    def test_incorrect_place_direction_command(self, caplog, test_input):
        caplog.set_level(logging.DEBUG)
        user_input = UserInput()
        user_input.process_file_line(test_input)
        assert (
            "Error in place command. Please ensure format is PLACE X, Y, F"
            in str(caplog.records)
        )

    # @pytest.mark.parametrize("test_input", [
    #     ('PLACE abc, 0, '),
    #     ('PLACE 0, abc, NORTH\n'),
    #     ('PLACE abc, abc, NORTH\n'),
    # ])
    # def test_incorrect_place_command(self, caplog, test_input):
    #     caplog.set_level(logging.DEBUG)
    #     list_line = test_input.rstrip('\n').split(" ")
    #     user_input = UserInput()
    #     result = user_input.handle_place(list_line)
    #     assert result is False
    #     assert (
    #             "Invalid data in PLACE command."
    #             in str(caplog.records)
    #     )
    #
    # @pytest.mark.parametrize("test_input", [
    #     (["MOVE"]),
    # ])
    # def test_handle_move_report_direction_empty_line(self, test_input):
    #     user_input = UserInput()
    #     result = user_input.handle_move(test_input)
    #     assert result is "MOVE"
    #
    #     result = user_input.handle_report(test_input)
    #     assert result is "MOVE"
    #
    #     result = user_input.handle_direction(test_input)
    #     assert result is "MOVE"
    #
    #     result = user_input.handle_empty_line(test_input)
    #     assert result is False