import logging

from toy_robot.table_top import TableTop
from toy_robot.robot import Robot
from toy_robot.user_input import UserInput
from toy_robot.table_top_positioner import Positioner, DirectionsEnum

logging.basicConfig(format='%(message)s', level=logging.INFO)
# The table dimensions
TABLE_TOP_LENGTH = 5
TABLE_TOP_WIDTH = 5


class CommandHandler:
    """
    Class to handle the user commands on the toy robot.
    """
    def __init__(self, file_name=None):
        self.table_top = TableTop(
            length=TABLE_TOP_LENGTH,
            width=TABLE_TOP_WIDTH
        )
        self._file_name = file_name,
        self.user_input = UserInput()
        self.robot = Robot()
        self.table_top_positioner = Positioner()

    def set_file_name(self, file_name) -> None:
        """
         Sets the value of the file path
        """
        self._file_name = file_name

    def get_file_name(self) -> str:
        """
        Returns the file path
        """
        return self._file_name

    def handle_place_command(self, command: list) -> None:
        """
        Handles the 'PLACE' command.

        This puts the robot within the tabletop dimensions

        :param command: list
        """
        move_x = command[1]
        move_y = command[2]
        can_place = self.table_top.validate_with_dimensions(move_x, move_y)
        if can_place:
            self.robot.set_positions(
                x=move_x,
                y=move_y,
                direction=DirectionsEnum[command[3]]
            )
            logging.info(f"PLACE: the robot on position: {self.robot.current_position()}")
        else:
            logging.warning(f'cannot move to coordinates: {move_x} {move_y} as it is outside tabletop')

    def handle_move_command(self) -> None:
        """
        Handles the `MOVE` command.

        The Positioner class calculates the new coordinates the robot has moved to then
        validates with the tabletop dimensions. If the validation passes, the new robot gets
        updated with the new coordinates.
        """
        move_x, move_y = self.table_top_positioner.position_updater(self.robot)
        can_move = self.table_top.validate_with_dimensions(move_x, move_y)
        if can_move:
            self.robot.set_x(move_x)
            self.robot.set_y(move_y)
        else:
            logging.info(f'Robot will go overboard with this move, current: {self.robot.current_position()}')

    def handle_left_command(self) -> None:
        """
        Handles the 'LEFT' command.
        Calculates whichever direction the robot's face has turned towards when the
        robot turns left.

        The logic is handled by the Positioner class
        """
        direction = self.table_top_positioner.handle_left_turn(self.robot)
        self.robot.set_direction(direction)

    def handle_right_command(self) -> None:
        """
        Handles the 'RIGHT' command.
        Calculates whichever direction the robot's face has turned toward when the
        robot turns right.

        The logic is handled by the Positioner class
        """
        direction = self.table_top_positioner.handle_right_turn(self.robot)
        self.robot.set_direction(direction)

    def handle_report_command(self) -> None:
        """
        Logs out the current robot position
        """
        logging.info(f"MOVED: {self.robot.current_position()}")

    def execute_command(self, command: list) -> None:
        """
        This function will load the handle function according to the command.
        A Place command will run the `handle_place_command` function,
        move command will run the 'handle_move_command' function, etc

        :param command: List
        """
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
