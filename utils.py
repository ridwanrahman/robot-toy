import os
from enum import Enum


class DirectionsEnum(Enum):
    """
    Enum to hold the different directions
    """
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def get_root_folder():
    """
    Get the root directory of the project.
    To maintain the same path to the root
    """
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    return ROOT_DIR
