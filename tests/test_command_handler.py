from toy_robot.robot import Robot
from toy_robot.command_handler import CommandHandler


class TestCommandHandler:

    def test_execute_command(self):
        command = ['PLACE', 0, 4, 'EAST']
        test_command_handler_class = CommandHandler()
        test_command_handler_class.execute_command(command)
        print("jkherer")