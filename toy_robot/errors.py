class PlaceCommandError(Exception):
    """
    Handles errors with PLACE command
    """
    pass


class EmptyCommandError(Exception):
    """
    Handles errors with empty lines
    """
    pass


class WrongCommandError(Exception):
    """
    Handles errors where the command is incorrect
    """
    pass
