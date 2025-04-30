import unittest
from src.engine.text_parser import TextParser

class TestTextParser(unittest.TestCase):

    def setUp(self):
        self.parser = TextParser()

    def test_parse_input_valid_command(self):
        command = "go north"
        expected_output = {"action": "go", "direction": "north"}
        self.assertEqual(self.parser.parse_input(command), expected_output)

    def test_parse_input_invalid_command(self):
        command = "fly to the moon"
        expected_output = None
        self.assertEqual(self.parser.parse_input(command), expected_output)

    def test_validate_command_valid(self):
        command = "take acorn"
        self.assertTrue(self.parser.validate_command(command))

    def test_validate_command_invalid(self):
        command = "jump over the river"
        self.assertFalse(self.parser.validate_command(command))

if __name__ == '__main__':
    unittest.main()