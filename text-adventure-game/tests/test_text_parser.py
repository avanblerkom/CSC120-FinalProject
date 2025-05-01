import unittest
import sys
import os

# Add the 'text-adventure-game' directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.engine.text_parser import TextParser

class TestTextParser(unittest.TestCase):
    """
    Unit tests for the TextParser class.
    """

    def setUp(self):
        """
        Set up a new instance of TextParser for each test.
        """
        self.text_parser = TextParser()

    def test_parse_input_with_action_and_direction(self):
        """
        Test parsing input with both an action and a direction.
        """
        command = "go north"
        expected_output = {"action": "go", "direction": "north"}
        self.assertEqual(self.text_parser.parse_input(command), expected_output)

    def test_parse_input_with_action_only(self):
        """
        Test parsing input with only an action.
        """
        command = "inventory"
        expected_output = {"action": "inventory"}
        self.assertEqual(self.text_parser.parse_input(command), expected_output)

    def test_parse_input_invalid(self):
        """
        Test parsing invalid input (empty string).
        """
        command = ""
        self.assertIsNone(self.text_parser.parse_input(command))

    def test_validate_command(self):
        """
        Test validating a command against a list of valid commands.
        """
        valid_commands = ["go", "take", "use", "inventory"]
        command = {"action": "go"}
        self.assertTrue(self.text_parser.validate_command(command, valid_commands))

if __name__ == '__main__':
    unittest.main()