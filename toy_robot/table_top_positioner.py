from utils import DirectionsEnum

from robot import Robot


class Positioner:
    """
    This class is in charge of applying the tabletop rules for the movement.
    """
    def __init__(self):
        pass

    def position_updater(self, robot: Robot) -> tuple[int, int]:
        """


        :param robot: Robot
        :return: x: int, y: int
        """
        move_x = None
        move_y = None
        if robot.get_direction().value == DirectionsEnum.NORTH.value:
            move_x = robot.get_x()
            move_y = 1 + robot.get_y()

        if robot.get_direction().value is DirectionsEnum.SOUTH.value:
            move_x = robot.get_x()
            move_y = robot.get_y() - 1

        if robot.get_direction().value is DirectionsEnum.EAST.value:
            move_x = 1 + robot.get_x()
            move_y = robot.get_y()

        if robot.get_direction().value is DirectionsEnum.WEST.value:
            move_x = robot.get_x() - 1
            move_y = robot.get_y()
        return move_x, move_y

    def handle_left_turn(self, robot: Robot):
        calculation = (robot.get_direction().value - 1) % 4
        return DirectionsEnum(calculation)

    def handle_right_turn(self, robot: Robot):
        calculation = (robot.get_direction().value + 1) % 4
        return DirectionsEnum(calculation)
