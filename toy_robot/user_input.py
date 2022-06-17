import logging

from typing import List, Optional, Union
from toy_robot.errors import PlaceCommandError, EmptyCommandError, WrongCommandError

logging.basicConfig(format='%(message)s', level=logging.INFO)
DIRECTIONS = ['NORTH', 'SOUTH', 'EAST', 'WEST']


class UserInput:
    """
    Class to handle user_inputs from .txt file
    """
    def __init__(self, file_name=None):
        self._file_name = file_name
        self._command_list = []

    def get_file_name(self) -> str:
        """
        Get the name of the file
        :return: str
        """
        return self._file_name

    def set_file_name(self, file_name: str) -> None:
        """
        Set the file name which needs to be in txt format
        :param file_name: str
        """
        if not file_name.endswith('.txt'):
            raise Exception
        self._file_name = file_name

    def get_command_list(self) -> list:
        """
        Return the command list
        """
        return self._command_list

    def append_into_command_list(self, command) -> None:
        """
        Append into command_list
        """
        self._command_list.append(command)

    def handle_place(self, list_line: list) -> list:
        """
        Handles the 'PLACE' command

        :param list_line: list
        :return: list
        """
        validated_list = []
        try:
            if list_line[0].upper() == 'PLACE' and list_line[3].upper() in DIRECTIONS:
                validated_list.append(list_line[0])
                num1 = list_line[1].split(",")
                num2 = list_line[2].split(",")
                validated_list.append(int(num1[0]))
                validated_list.append(int(num2[0]))
                validated_list.append(list_line[3])
                return validated_list
            else:
                raise PlaceCommandError("ERROR: Please ensure format is PLACE X, Y, F, as program starts after PLACE command")
        except Exception as pl:
            raise PlaceCommandError("ERROR: Please ensure format is PLACE X, Y, F, as program starts after PLACE command")

    def handle_move(self, list_line: list) -> str:
        """
        Handles the 'MOVE' command

        :param list_line: str
        :return: str
        """
        if len(list_line) > 1:
            raise WrongCommandError("ERROR: Incorrect MOVE command provided in input file")
        if list_line[0].upper() == 'MOVE':
            return str(list_line[0]).upper()
        else:
            raise KeyError

    def handle_report(self, list_line: list) -> str:
        """
        Handles the 'REPORT' command
        :param list_line: str
        :return: str
        """
        if len(list_line) > 1:
            raise WrongCommandError("ERROR: Incorrect REPORT command provided in input file")
        if list_line[0].upper() == 'REPORT':
            return str(list_line[0]).upper()
        raise KeyError

    def handle_direction(self, list_line: list) -> str:
        """
        Handles if the direction is either LEFT/RIGHT

        :param list_line: str
        :return: str
        """
        if len(list_line) > 1:
            raise WrongCommandError("ERROR: Incorrect LEFT/RIGHT command provided in input file")
        if list_line[0].upper() in ['LEFT', 'RIGHT']:
            return str(list_line[0]).upper()
        raise KeyError

    def handle_empty_line(self, list_line: str):
        """
        Empty lines should raise an error

        :param list_line: str
        """
        raise EmptyCommandError("ERROR: Empty line present in input file")

    def list_append(self, record: Union[str, list]) -> None:
        """
        Append into command_list list to create a list of commands.
        """
        if 'PLACE' in record or 'place' in record:
            self.append_into_command_list(record)
        else:
            if not self.get_command_list():
                return
            self.append_into_command_list(record)

    def process_file_line(self, line: Union[str, list]) -> None:
        """
        Process the command according to the first command in each line

        :param line: str
        """
        validation_handlers = {
            'PLACE': self.handle_place,
            'MOVE': self.handle_move,
            'REPORT': self.handle_report,
            'LEFT': self.handle_direction,
            'RIGHT': self.handle_direction,
            '': self.handle_empty_line
        }
        try:
            line = line.rstrip('\n')
            list_line = line.split(" ")
            first_word = list_line[0].upper()
            validated_record = validation_handlers[first_word](list_line)
            if validated_record:
                self.list_append(validated_record)
        except Exception as e:
            if isinstance(e, KeyError):
                logging.warning(f'ERROR: Incorrect command: {line}')
            else:
                logging.warning(e)

    def open_and_read_file(self) -> None:
        """
        Open the file and read each line and send to `process_file_line()` function to process
        and validate the line
        """
        try:
            with open(self.get_file_name()) as file:
                for line in file:
                    self.process_file_line(line)
        except FileNotFoundError:
            logging.warning(f'File not found')
