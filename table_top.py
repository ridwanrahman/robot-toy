class TableTop:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_table_top_dimensions(self) -> tuple:
        return self._length, self._width

    def validate_with_dimensions(self, x: int, y: int) -> bool:
        return (0 <= x <= self._length) and (0 <= y <= self._width)
