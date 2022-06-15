import logging

from table_top import TableTop
from robot import Robot
from user_input import UserInput


TABLE_TOP_LENGTH = 5
TABLE_TOP_WIDTH = 5
logger = logging.getLogger(__name__)


class Game:
    def __init__(self):
        pass

    def handle_place_command(self):
        pass

    def handle_move_command(self):
        pass

    def handle_left_command(self):
        pass

    def handle_right_command(self):
        pass

    def move(self, command):
        pass

    def play_game(self):
        pass

def main():
    game = Game()
    game.play_game()

if __name__ == '__main__':
    main()