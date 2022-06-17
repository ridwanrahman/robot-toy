import os
import logging
import utils

from toy_robot.command_handler import CommandHandler


class TestEndToEnd:

    def test_end_to_end_1(self, caplog):
        caplog.set_level(logging.INFO)

        # Load the txt file
        root_folder = utils.get_root_folder()
        file_path = os.path.join(root_folder, 'resources/test_inputs/test_user_inputs_1.txt')

        test_command_class = CommandHandler()
        test_command_class.set_file_path(file_path)
        test_command_class.command_runner()
        assert (
                "OUTPUT : 1, 4, EAST"
                in str(caplog.records)
        )

    def test_end_to_end_2(self, caplog):
        caplog.set_level(logging.INFO)

        # Load the txt file
        root_folder = utils.get_root_folder()
        file_path = os.path.join(root_folder, 'resources/test_inputs/test_user_inputs_2.txt')

        test_command_class = CommandHandler()
        test_command_class.set_file_path(file_path)
        test_command_class.command_runner()
        assert (
                "OUTPUT : 3, 3, NORTH"
                in str(caplog.records)
        )

