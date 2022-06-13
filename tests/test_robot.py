import pytest

from robot import Robot
from utils import DirectionsEnum


class TestRobot:
    def test_create_robot(self):
        """
        This test will create a test robot instance and set its positions and assert
        if the positions have been set
        """
        test_robot = Robot()
        test_robot.set_positions(
            x=1,
            y=2,
            direction=DirectionsEnum.SOUTH
        )
        assert (test_robot.get_x() == 1)
        assert (test_robot.get_y() == 2)
        assert (test_robot.get_direction() == DirectionsEnum.SOUTH)
