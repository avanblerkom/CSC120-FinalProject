import unittest
from src.engine.story_engine import StoryEngine

class TestStoryEngine(unittest.TestCase):
    """
    Unit tests for the StoryEngine class.
    """

    def setUp(self):
        """
        Set up a new instance of StoryEngine with sample data for each test.
        """
        self.sample_data = {
            "locations": {
                "start": {
                    "story": {"text": "Welcome to the start."},
                    "choices": [{"text": "Go to forest", "next_location": "forest"}]
                },
                "forest": {
                    "story": {"text": "You are in a forest."},
                    "choices": []
                }
            }
        }
        self.story_engine = StoryEngine(self.sample_data)

    def test_load_location(self):
        """
        Test loading a location by its ID.
        """
        self.story_engine.load_location("start")
        self.assertEqual(self.story_engine.get_story_text(), "Welcome to the start.")

    def test_get_choices(self):
        """
        Test retrieving choices for a loaded location.
        """
        self.story_engine.load_location("start")
        choices = self.story_engine.get_choices()
        self.assertEqual(len(choices), 1)
        self.assertEqual(choices[0]["text"], "Go to forest")

if __name__ == '__main__':
    unittest.main()