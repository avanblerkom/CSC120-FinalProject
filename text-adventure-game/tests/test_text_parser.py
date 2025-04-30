import unittest
import sys
import os


# Add the 'text-adventure-game' directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.engine.text_parser import TextParser


class TestTextParser(unittest.TestCase):

    def setUp(self):
        self.parser = TextParser()

    def test_parse_input_with_action_and_direction(self):
        command = "go north"
        expected_output = {"action": "go", "direction": "north"}
        self.assertEqual(self.parser.parse_input(command), expected_output)

    def test_parse_input_with_action_only(self):
        command = "inventory"
        expected_output = {"action": "inventory"}
        self.assertEqual(self.parser.parse_input(command), expected_output)

    def test_parse_input_invalid(self):
        command = ""
        self.assertIsNone(self.parser.parse_input(command))

    def test_validate_command(self):
        valid_commands = ["go", "take", "use", "inventory"]
        command = {"action": "go"}
        self.assertTrue(self.parser.validate_command(command, valid_commands))

if __name__ == '__main__':
    unittest.main()