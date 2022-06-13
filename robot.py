from utils import DirectionsEnum

class Robot:
    def __init__(self, x=None, y=None, direction=None):
        self._x = x
        self._y = y
        self._direction = direction

    def current_position(self):
        return self._x, self._y, self._direction.name

    def set_positions(self, x: int, y: int, direction: DirectionsEnum):
        self._x = x
        self._y = y
        self._direction = direction

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def set_x(self, x: int) -> None:
        self._x = x

    def set_y(self, y: int) -> None:
        self._y = y

    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction