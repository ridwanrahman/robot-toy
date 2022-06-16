import os

from utils import get_root_folder

from toy_robot.command_handler import CommandHandler

# Change the file name here. Please ensure to put the txt file inside resources folder
# A sample user_input.txt file is provided inside the resources folder
FILE_PATH = 'resources/user_input.txt'


class Runner:
    """
    Please run this file to start the app

    Class to inject the path of the file and start the app
    """
    def run_robot_app(self):
        """
        Creates the CommandHandler class and calls teh command_runner() function
        """
        root_folder = get_root_folder()
        file_path = os.path.join(root_folder, FILE_PATH)

        command_handle_class = CommandHandler()
        command_handle_class.set_file_name(file_path)
        command_handle_class.command_runner()


def main():
    runner = Runner()
    runner.run_robot_app()


if __name__ == '__main__':
    main()
