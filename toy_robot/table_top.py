class TableTop:
    """
    A class to represent the table top where the robot moves
    """
    def __init__(self, length, width):
        """
        Parameters
        ----------
        length: int
        width: int
        """
        self._length = length
        self._width = width

    def get_length(self) -> int:
        """
        Returns length of the table top

        :return: int
        """
        return self._length

    def get_width(self) -> int:
        """
        Returns the width of the table top

        :return: int
        """
        return self._width

    def get_table_top_dimensions(self) -> tuple:
        """
        Returns the length and width of the table
        """
        return self._length, self._width

    def validate_with_dimensions(self, x: int, y: int) -> bool:
        """
        Checks whether the value of x and y is inside the tabletop.

        Parameters
        ----------
        x: int
            the x value of the robot where it should move to
        y: int
            the y value of the robot where it should move to
        returns: bool
            returns True/False depending on whether the robot
            is within the dimensions of the tabletop
        """
        return (0 <= x <= self._length) and (0 <= y <= self._width)
