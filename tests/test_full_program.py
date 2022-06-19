import os
import logging
import utils

from toy_robot.command_handler import CommandHandler


class TestEndToEnd:
    """
    This test class will test the whole program from start to end.

    The program starts from runner class which calls CommandHandler. The tests
    provided here also call CommandHandler and inject file path
    """

    def test_end_to_end_1(self, caplog):
        """
        Direct the file path to the test file and initialize CommandHandler() with the
        test inputs and then assert with the output
        """
        caplog.set_level(logging.INFO)

        # Load the test txt file
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
        """
        Direct the file path to the test file and initialize CommandHandler() with the
        test inputs and then assert with the output
        """
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

