from utils import DirectionsEnum

from toy_robot.robot import Robot


class Positioner:
    """
    This class is in charge of applying the tabletop rules for the movement.
    """
    def __init__(self):
        pass

    def position_updater(self, robot: Robot) -> tuple[int, int]:
        """
        Every time the robot is allowed to move, this function calculates the coordinates it will move
        to. It takes into consideration the direction the robot is facing. Then calculates the x and y coordinates
        accordingly.

        :param robot: Robot
        :return: x: int, y: int
        """
        move_x = None
        move_y = None
        if robot.get_direction().value == DirectionsEnum.NORTH.value:
            # The north direction is in the Y-axis and going north will
            # increment the y value
            move_x = robot.get_x()
            move_y = 1 + robot.get_y()

        if robot.get_direction().value is DirectionsEnum.SOUTH.value:
            # The south direction is in the Y-axis and going south will
            # decrement the y value
            move_x = robot.get_x()
            move_y = robot.get_y() - 1

        if robot.get_direction().value is DirectionsEnum.EAST.value:
            # The east direction is in the x-axis and going east will
            # increment the x value
            move_x = 1 + robot.get_x()
            move_y = robot.get_y()

        if robot.get_direction().value is DirectionsEnum.WEST.value:
            # The west direction is in the x-axis and going west will
            # decrement the x value
            move_x = robot.get_x() - 1
            move_y = robot.get_y()
        return move_x, move_y

    def handle_left_turn(self, robot: Robot):
        # To turn left, decrement the value and mod with 4
        calculation = (robot.get_direction().value - 1) % 4
        return DirectionsEnum(calculation)

    def handle_right_turn(self, robot: Robot):
        # To turn right, increment the value and mod with 4
        calculation = (robot.get_direction().value + 1) % 4
        return DirectionsEnum(calculation)
