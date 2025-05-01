class TextParser:
    """
    A class to parse and validate user input for the text-based adventure game.
    """

    def __init__(self):
        """
        Initialize the TextParser instance.
        """
        pass

    def parse_input(self, user_input):
        """
        Parse the user's input into an action and optional direction.

        Args:
            user_input (str): The raw input string from the user.

        Returns:
            dict: A dictionary containing the action and direction (if applicable).
                  Returns None if the input is invalid.
        """
        words = user_input.strip().lower().split()
        if len(words) >= 2:
            return {"action": words[0], "direction": words[1]}
        elif len(words) == 1:
            return {"action": words[0]}
        return None

    def validate_command(self, command, valid_commands):
        """
        Validate the parsed command against a list of valid commands.

        Args:
            command (dict): The parsed command dictionary.
            valid_commands (list): A list of valid action strings.

        Returns:
            bool: True if the command is valid, False otherwise.
        """
        if not valid_commands or not isinstance(command, dict) or "action" not in command:
            return False
        return command["action"] in valid_commands