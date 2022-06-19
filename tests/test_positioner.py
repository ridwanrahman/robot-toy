import pytest

from utils import DirectionsEnum

from toy_robot.robot import Robot
from toy_robot.table_top_positioner import Positioner


class TestPositioner:

    @pytest.mark.parametrize("test_input, expected", [
        ([0, 0, DirectionsEnum.SOUTH], [0, -1]),
        ([3, 3, DirectionsEnum.WEST], [2, 3]),
        ([2, 2, DirectionsEnum.EAST], [3, 2]),
        ([4, 4, DirectionsEnum.NORTH], [4, 5])
    ])
    def test_positioner(self, test_input, expected):
        """
         The Positioner class is in charge of generating the new positions of the robot in the
         direction whichever the robot is facing. it will return the new x and y coordinates
        """
        test_robot = Robot()
        test_robot.set_positions(test_input[0], test_input[1], test_input[2])

        positioner = Positioner()
        move_x, move_y = positioner.position_updater(test_robot)
        assert (move_x == expected[0])
        assert (move_y == expected[1])

    @pytest.mark.parametrize("test_input, expected", [
        ([0, 0, DirectionsEnum.NORTH], DirectionsEnum.WEST),
        ([0, 0, DirectionsEnum.SOUTH], DirectionsEnum.EAST),
        ([0, 0, DirectionsEnum.EAST], DirectionsEnum.NORTH),
        ([0, 0, DirectionsEnum.WEST], DirectionsEnum.SOUTH),
    ])
    def test_handle_left(self, test_input, expected):
        """
        Test the positioner class's handle_left_turn method.
        The input data will turn towards its left direction

        E.g. NORTH -> TURN LEFT -> WEST
        """
        test_robot = Robot()
        test_robot.set_positions(test_input[0], test_input[1], test_input[2])

        positioner = Positioner()
        new_direction = positioner.handle_left_turn(test_robot)
        assert (new_direction == expected)

    @pytest.mark.parametrize("test_input, expected", [
        ([0, 0, DirectionsEnum.NORTH], DirectionsEnum.EAST),
        ([0, 0, DirectionsEnum.SOUTH], DirectionsEnum.WEST),
        ([0, 0, DirectionsEnum.EAST], DirectionsEnum.SOUTH),
        ([0, 0, DirectionsEnum.WEST], DirectionsEnum.NORTH),
    ])
    def test_handle_right(self, test_input, expected):
        """
        Test the positioner class's handle_right_turn method.
        The input data will turn towards its right direction

        E.g. NORTH -> TURN RIGHT -> EAST
        """
        test_robot = Robot()
        test_robot.set_positions(test_input[0], test_input[1], test_input[2])

        positioner = Positioner()
        new_direction = positioner.handle_right_turn(test_robot)
        assert (new_direction == expected)
