class TextParser:
    def __init__(self):
        pass

    def parse_input(self, user_input):
        # Map input to action and direction if applicable
        words = user_input.strip().lower().split()
        if len(words) >= 2:
            return {"action": words[0], "direction": words[1]}
        elif len(words) == 1:
            return {"action": words[0]}
        return None

    def validate_command(self, command, valid_commands):
        # Check if the command is valid
        if not valid_commands or not isinstance(command, dict) or "action" not in command:
            return False
        return command["action"] in valid_commands