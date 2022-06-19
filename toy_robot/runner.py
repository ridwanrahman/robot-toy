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

    N.B test not included for this class as it only runs the program
    """
    def run_robot_app(self) -> None:
        """
        Creates the CommandHandler class and calls teh command_runner() function
        """
        # Get the root folder of the project and append the path to the resource folder
        root_folder = get_root_folder()
        file_path = os.path.join(root_folder, FILE_PATH)

        # Create a CommandHandler class
        command_handle_class = CommandHandler()
        # inject the path of the file to command handler class which in turn
        # will inject to the UserInput() class
        command_handle_class.set_file_path(file_path)
        # run the command handler class to read the input, validate, and move the robot
        command_handle_class.command_runner()


def main():
    runner = Runner()
    runner.run_robot_app()


if __name__ == '__main__':
    main()
