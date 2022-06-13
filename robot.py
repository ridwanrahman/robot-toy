from utils import DirectionsEnum


class Robot:
    """
    A class to represent a Robot

    Attributes
    ----------
    x: int
        the integer value of x coordinate on a tabletop
    y: int
        the integer value of y coordinate on a tabletop
    direction: enum
        the direction that the robot is facing (enum values: NORTH, SOUTH, EAST, WEST)
    """
    def __init__(self, x=None, y=None, direction=None):
        """
        Parameters
        ----------
        x: int
            x coordinate on tabletop
        y: int
            y coordinate on tabletop
        direction: enum value
            direction the robot will face
        """
        self._x = x
        self._y = y
        self._direction = direction

    def current_position(self) -> tuple:
        """
        Returns the current position of the robot
        :return: tuple (x: int, y: int, direction: enum)
        """
        return self._x, self._y, self._direction.name

    def set_positions(self, x: int, y: int,
                      direction: DirectionsEnum) -> None:
        """
        Sets the position of a robot

        Parameters
        ----------
        x: int
        y: int
        direction: enum
        """
        self._x = x
        self._y = y
        self._direction = direction

    def get_x(self) -> int:
        """
        Returns value of x coordinate of robot
        """
        return self._x

    def get_y(self) -> int:
        """
        Returns value of y coordinate of robot
        """
        return self._y

    def set_x(self, x: int) -> None:
        """
        Sets the x coordinate value of robot

        x: int
        """
        self._x = x

    def set_y(self, y: int) -> None:
        """
        Sets the y coordinate value of robot
        """
        self._y = y

    def get_direction(self) -> DirectionsEnum:
        """
        Returns the enum of the direction
        """
        return self._direction

    def set_direction(self, direction: DirectionsEnum) -> None:
        """
        Sets the direction the robot is facing

        Parameters
        ----------
        direction: DirectionsEnum
        """
        self._direction = direction
