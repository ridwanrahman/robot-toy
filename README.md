# Robot Toy Challenge

## Description
This app is the implementation of the toy robot challenge.

## Requirements
1. Pycharm (Vscode can be used too but the virtualenv setup can be different)
2. python 3.9
3. pytest
4. pytest-cov

## Setup Instructions
1. Clone from git
2. Open the project in pycharm. 
Pycharm will create either a virtualenv/ anaconda env.
3. run `pip install -r requirements.txt` to install the requirements.
4. Open the `runner.py` file and run it.
5. Some movement results should show up on the terminal.

## Implementation
1. This app was built with the idea of modularity and reusability in mind.
2. To run, please start with some basic commands in `resources/user_input.txt`. Let's say we begin with
the following:
```
PLACE 0, 0, F
MOVE
LEFT
RIGHT
REPORT
```
The result of the command above would be:
```
-------------------------
COMMAND: PLACE
RESULT : Placed robot on position: 0, 0, NORTH
COMMAND: MOVE
COMMAND: LEFT
COMMAND: RIGHT
COMMAND: REPORT
RESULT : 0, 1, NORTH
```
The structure of the terminal output shows each command and its result.
3. In the below command, there is a wrong command on line 2 as below:
```
PLACE 1, 0, NORTH
not-move
LEFT
RIGHT
REPORT
```
The terminal output would show the errors at first then the output of the program
as below:
```
ERROR: Incorrect command: not-move
-------------------------
COMMAND: PLACE
RESULT : Placed robot on position: 1, 0, NORTH
COMMAND: LEFT
COMMAND: RIGHT
COMMAND: REPORT
RESULT : 1, 0, NORTH
```

## Testing

Pytest was used to write tests for this program. To run the tests: 

``python -m pytest -s tests``

To get a coverage report, please run:

1. ``coverage run --source=toy_robot -m pytest -v tests``

2. ``coverage report``

3. ``coverage report --show-missing`` (to get the lines that are missing)

## Project Structure

### Folder structure
```
├── toy_robot
    └── resources
        └── test_inputs
            └── test_user_inputs_1.txt
            └── test_user_inputs_2.txt
        └── user_input.txt
    └── tests
        └── __init__.py
        └── test_command.py
        └── test_full_program.py
        └── test_positioner.py
        └── test_robot.py
        └── test_table_top.py
        └── test_user_input.py
    └── toy_robot
        └── __init__.py
        └── command_handler.py
        └── errors.py
        └── robot.py
        └── runner.py
        └── table_top.py
        └── table_top_positioner.py
        └── user_input.py
    └── README.md
    └── requirements.txt
    └── utils
```
## 
1. The toy_robot folder holds all the classes for the robot challenge.
   1. Running the runner class will load the `user_input.txt` from the resources
   folder in the root directory. (This app was written in mac and not tested in windows).
   To change the app to read from any other files, please copy to resources folder and write
   the new file's name in runner class.
   2. The runner creates `CommandHandler` class. Then it sets the file_path to the file variable in
   `CommandHandler`. Then it calls the `CommandHandler.command_runner()`
   3. The `command_runner()` function creates the UserInput class by injecting the
   file_path, loads the file and validates it and sends a list of allowed commands.
   The allowed commands follow the rules that are mentioned in the rules. E.g. the first command 
    has to be a 'PLACE' command and any commands before that is ignored, etc.
   4. It returns the validated list of commands, and command_runnder executes each of those commands
   and updates the position of the robot accordingly while checking if the movement is allowed.
2. The tests folder contains all the tests. The test data are being entered
from `resources/test_inputs/...`