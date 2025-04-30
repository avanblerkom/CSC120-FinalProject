import unittest
import sys
import os

# Add the 'text-adventure-game' directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.engine.game_state import GameState

class TestGameState(unittest.TestCase):

    def setUp(self):
        self.game_state = GameState()

    def test_initial_inventory(self):
        self.assertEqual(self.game_state.inventory, {})  # Inventory should be a dictionary

    def test_update_inventory(self):
        self.game_state.update_inventory('wood')
        self.assertEqual(self.game_state.inventory['wood'], 1)

    def test_update_location(self):
        self.game_state.update_location("forest")
        self.assertEqual(self.game_state.get_location(), "forest")

    def test_mark_puzzle_completed(self):
        self.game_state.mark_puzzle_completed(1)
        self.assertTrue(self.game_state.is_puzzle_completed(1))

if __name__ == '__main__':
    unittest.main()