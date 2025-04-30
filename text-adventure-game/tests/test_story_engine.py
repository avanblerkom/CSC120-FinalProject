import unittest
from src.engine.story_engine import StoryEngine

class TestStoryEngine(unittest.TestCase):

    def setUp(self):
        self.story_engine = StoryEngine()
        self.story_engine.load_story('path/to/story_scripts.json')  # Adjust the path as necessary

    def test_get_choices(self):
        choices = self.story_engine.get_choices('some_story_point')
        self.assertIsInstance(choices, list)
        self.assertGreater(len(choices), 0)

    def test_make_choice(self):
        initial_state = self.story_engine.current_state
        self.story_engine.make_choice('valid_choice')
        self.assertNotEqual(initial_state, self.story_engine.current_state)

    def test_load_story(self):
        self.story_engine.load_story('path/to/story_scripts.json')
        self.assertIsNotNone(self.story_engine.story_data)

if __name__ == '__main__':
    unittest.main()