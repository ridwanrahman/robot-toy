import pytest
import logging

from toy_robot.command_handler import CommandHandler


class TestEndToEnd:

    def test_end_to_end_1(self, caplog):
        caplog.set_level(logging.INFO)
        file_name = '../resources/test_inputs/test_user_inputs_1.txt'
        test_command_class = CommandHandler()
        test_command_class.set_file_name(file_name)
        test_command_class.command_runner()
        assert (
                "1, 4, EAST"
                in str(caplog.records)
        )

    def test_end_to_end_2(self, caplog):
        caplog.set_level(logging.INFO)
        file_name = '../resources/test_inputs/test_user_inputs_2.txt'
        test_command_class = CommandHandler()
        test_command_class.set_file_name(file_name)
        test_command_class.command_runner()
        assert (
                "3, 3, NORTH"
                in str(caplog.records)
        )

