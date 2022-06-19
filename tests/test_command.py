import pytest
import logging

from utils import DirectionsEnum

from toy_robot.command_handler import CommandHandler


class TestCommand:
    @pytest.mark.parametrize("test_input, expected", [
        (['PLACE', 0, 0, 'NORTH'], [0, 0, DirectionsEnum.NORTH]),
        (['PLACE', 1, 2, 'WEST'], [1, 2, DirectionsEnum.WEST]),
        ('MOVE', [None, None, None]),
        ('LEFT', [None, None, None]),
        ('RIGHT', [None, None, None])
    ])
    def test_execute_command(self, test_input, expected):
        """
        Every time a robot is created, the first command has to be 'PLACE' to put the robot in a location.
        If the commands are move/left/right, the robots position will not change,
        """
        test_command = CommandHandler()
        test_command.execute_command(test_input)
        assert (test_command.robot.get_x() == expected[0])
        assert (test_command.robot.get_y() == expected[1])
        assert (test_command.robot.get_direction() == expected[2])

    @pytest.mark.parametrize("initial, test_input, expected", [
        (['PLACE', 0, 0, 'NORTH'], 'MOVE', [0, 1, DirectionsEnum.NORTH]),
        (['PLACE', 1, 1, 'EAST'], 'MOVE', [2, 1, DirectionsEnum.EAST]),
        (['PLACE', 1, 1, 'EAST'], 'LEFT', [1, 1, DirectionsEnum.NORTH]),
        (['PLACE', 1, 1, 'EAST'], 'RIGHT', [1, 1, DirectionsEnum.SOUTH]),
        (['PLACE', 1, 1, 'SOUTH'], 'MOVE', [1, 0, DirectionsEnum.SOUTH]),
    ])
    def test_move_commands(self, initial, test_input, expected):
        """
        Test with initial data and check to see if the robot has moved to the
        expected direction
        """
        test_command = CommandHandler()
        test_command.execute_command(initial)
        test_command.execute_command(test_input)
        assert (test_command.robot.get_x() == expected[0])
        assert (test_command.robot.get_y() == expected[1])
        assert (test_command.robot.get_direction() == expected[2])

    @pytest.mark.parametrize("test_input, expected", [
        (['PLACE', 5, 5, 'WEST'], [5, 5, DirectionsEnum.WEST]),
        (['PLACE', 10, 10, 'EAST'], [None, None, None]),
    ])
    def test_handle_place_command(self, test_input, expected):
        """
        To test the handle place command which sets the initial position of the robot.
        If the coordinates are outside the tabletop (5*5), the robot will not be set
        """
        test_command = CommandHandler()
        test_command.handle_place_command(test_input)
        assert (test_command.robot.get_x() == expected[0])
        assert (test_command.robot.get_y() == expected[1])
        assert (test_command.robot.get_direction() == expected[2])

    @pytest.mark.parametrize("test_input, expected", [
        (['PLACE', 5, 5, 'WEST'], "5, 5, WEST"),
        (['PLACE', 0, 0, 'NORTH'], "0, 0, NORTH"),
    ])
    def test_handle_report_command(self, caplog, test_input, expected):
        """
        Testing the REPORT command to check if the right output is shown
        """
        caplog.set_level(logging.INFO)
        test_command = CommandHandler()
        test_command.handle_place_command(test_input)
        test_command.handle_report_command()
        assert (
                expected
                in str(caplog.records)
        )
