import unittest
import sys
import os

# Add the 'text-adventure-game' directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.engine.game_state import GameState

class TestGameState(unittest.TestCase):
    """
    Unit tests for the GameState class.
    """

    def setUp(self):
        """
        Set up a new instance of GameState for each test.
        """
        self.game_state = GameState()

    def test_initial_inventory(self):
        """
        Test that the initial inventory is empty.
        """
        self.assertEqual(self.game_state.inventory, {})

    def test_update_inventory(self):
        """
        Test adding an item to the inventory.
        """
        self.game_state.update_inventory('wood')
        self.assertEqual(self.game_state.inventory['wood'], 1)

    def test_update_location(self):
        """
        Test updating the player's current location.
        """
        self.game_state.update_location("forest")
        self.assertEqual(self.game_state.get_location(), "forest")

    def test_mark_puzzle_completed(self):
        """
        Test marking a puzzle as completed.
        """
        self.game_state.mark_puzzle_completed(1)
        self.assertTrue(self.game_state.is_puzzle_completed(1))

if __name__ == '__main__':
    unittest.main()