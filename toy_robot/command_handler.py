import os
import logging

import utils
from toy_robot.table_top import TableTop
from toy_robot.robot import Robot
from toy_robot.user_input import UserInput
from toy_robot.table_top_positioner import Positioner, DirectionsEnum

TABLE_TOP_LENGTH = 5
TABLE_TOP_WIDTH = 5
logging.basicConfig(level=logging.INFO)


class CommandHandler:
    def __init__(self, file_name=None):

        self.table_top = TableTop(
            length=TABLE_TOP_LENGTH,
            width=TABLE_TOP_WIDTH
        )
        self._file_name = file_name,
        self.user_input = UserInput()
        self.robot = Robot()
        self.table_top_positioner = Positioner()

    def set_file_name(self, file_name):
        self._file_name = file_name

    def get_file_name(self):
        return self._file_name

    def handle_place_command(self, command: list):
        move_x = command[1]
        move_y = command[2]
        can_move = self.table_top.validate_with_dimensions(move_x, move_y)
        if can_move:
            self.robot.set_positions(
                x=move_x,
                y=move_y,
                direction=DirectionsEnum[command[3]]
            )
        else:
            logging.warning(f'cannot move to coordinates: {move_x} {move_y} as it is outside tabletop')

    def handle_move_command(self):
        move_x, move_y = self.table_top_positioner.position_updater(self.robot)
        can_move = self.table_top.validate_with_dimensions(move_x, move_y)
        if can_move:
            self.robot.set_x(move_x)
            self.robot.set_y(move_y)

    def handle_left_command(self):
        direction = self.table_top_positioner.handle_left_turn(self.robot)
        self.robot.set_direction(direction)

    def handle_right_command(self):
        direction = self.table_top_positioner.handle_right_turn(self.robot)
        self.robot.set_direction(direction)

    def handle_report_command(self) -> None:
        logging.info(self.robot.current_position())

    def execute_command(self, command):
        movements = {
            'PLACE': self.handle_place_command,
            'MOVE': self.handle_move_command,
            'LEFT': self.handle_left_command,
            'RIGHT': self.handle_right_command,
            'REPORT': self.handle_report_command
        }
        if isinstance(command, list):
            movement_command = command[0]
            movements[movement_command](command)
        if isinstance(command, str):
            if self.robot.get_direction() is None:
                # if the robot is not on the tabletop, all commands are ignored
                return
            movements[command]()

    def command_runner(self):
        """
        The main command handler method that takes in validated user commands then executes each command
        """
        # Set the file name to user_input class
        self.user_input.set_file_name(self.get_file_name())

        # calling the open_and_read_file() will read the file, validate the inputs and only the commands that appear
        # after 'PLACE'
        self.user_input.open_and_read_file()
        # load the validated list of commands
        validated_user_commands = self.user_input.get_command_list()
        if len(validated_user_commands) == 0:
            logging.warning("Command list is empty, Please place correct command according to documentation")
            exit()
        # loop through and execute each command
        for command in validated_user_commands:
            self.execute_command(command)


def main():
    root_folder = utils.get_root_folder()
    file_path = os.path.join(root_folder, 'resources/user_input.txt')

    command_handle_class = CommandHandler()
    command_handle_class.set_file_name(file_path)
    command_handle_class.command_runner()

if __name__ == '__main__':
    main()
