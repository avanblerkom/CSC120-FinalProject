import unittest
from src.engine.game_state import GameState

class TestGameState(unittest.TestCase):

    def setUp(self):
        self.game_state = GameState()

    def test_initial_inventory(self):
        self.assertEqual(self.game_state.inventory, [])

    def test_update_inventory(self):
        self.game_state.update_inventory('wood')
        self.assertIn('wood', self.game_state.inventory)

    def test_save_state(self):
        self.game_state.update_inventory('stone')
        saved_state = self.game_state.save_state()
        self.assertEqual(saved_state['inventory'], ['stone'])

    def test_load_state(self):
        self.game_state.update_inventory('water')
        saved_state = self.game_state.save_state()
        new_game_state = GameState()
        new_game_state.load_state(saved_state)
        self.assertIn('water', new_game_state.inventory)

    def test_update_location(self):
        self.game_state.update_location("forest")
        self.assertEqual(self.game_state.get_location(), "forest")

    def test_navigation(self):
        self.game_state.update_location("start")
        self.assertEqual(self.game_state.get_location(), "start")
        self.game_state.update_location("forest")
        self.assertEqual(self.game_state.get_location(), "forest")
        self.game_state.update_location("start")
        self.assertEqual(self.game_state.get_location(), "start")
        self.game_state.update_location("river")
        self.assertEqual(self.game_state.get_location(), "river")

if __name__ == '__main__':
    unittest.main()