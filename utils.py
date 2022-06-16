import os
from enum import Enum


class DirectionsEnum(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def get_root_folder():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    return ROOT_DIR
